from __future__ import annotations

from abc import ABC, abstractmethod
from time import perf_counter

from app.ai.clients.llm_client import LLMClient
from app.ai.governance.guardrail_pipeline import GuardrailPipeline
from app.ai.agents.recovery_agent import RecoveryAgent

from app.ai.models.agent_error import (
    AgentError,
    ErrorType,
)

from app.ai.models.agent_metadata import AgentMetadata
from app.ai.models.agent_request import AgentRequest
from app.ai.models.agent_response import AgentResponse

from app.models.control_tower_context import Shipment, ShipmentEvent


class BaseAgent(ABC):

    def __init__(
        self,
        llm_client: LLMClient | None,
        guardrails: list,
        validators: list,
    ):

        self.llm_client = llm_client

        self.guardrail_pipeline = GuardrailPipeline(
            guardrails,
        )

        self.validators = validators

        self.recovery_agent = RecoveryAgent()

    @property
    @abstractmethod
    def agent_name(self) -> str:
        """Unique name of the agent."""
        pass

    @abstractmethod
    def execute(
        self,
        request: AgentRequest,
    ) -> dict:
        """
        Child agents implement only their business logic.
        """
        pass

    # ----------------------------------------------------
    # Helpers
    # ----------------------------------------------------

    def get_tracking(
        self,
        request: AgentRequest,
    ) -> dict:

        tracking = request.payload.get(
            "tracking",
        )

        if tracking is None:

            raise ValueError(
                "Tracking data not found in request payload."
            )

        return tracking

    def get_shipment(
        self,
        request: AgentRequest,
    ) -> Shipment:

        tracking = self.get_tracking(
            request,
        )

        shipment = tracking.get(
            "shipment",
        )

        if shipment is None:

            raise ValueError(
                "Shipment not found in tracking payload."
            )

        return Shipment.model_validate(
            shipment,
        )

    def get_events(
        self,
        request: AgentRequest,
    ) -> list[ShipmentEvent]:

        tracking = self.get_tracking(
            request,
        )

        events = tracking.get(
            "events",
            [],
        )

        return [
            ShipmentEvent.model_validate(
                event,
            )
            for event in events
        ]

    # ----------------------------------------------------
    # Pipeline
    # ----------------------------------------------------

    def run(
        self,
        request: AgentRequest,
    ) -> AgentResponse:

        return self._run_pipeline(
            request=request,
            retry_count=0,
        )

    def _run_pipeline(
        self,
        request: AgentRequest,
        retry_count: int,
    ) -> AgentResponse:

        start_time = perf_counter()

        #
        # Guardrails
        #

        guardrail_results = (
            self.guardrail_pipeline.validate(
                request,
            )
        )

        for result in guardrail_results:

            if not result.passed:

                return AgentResponse(
                    success=False,
                    payload=None,
                    metadata=AgentMetadata(
                        agent_name=self.agent_name,
                        model_name=(
                            self.llm_client.model_name
                            if self.llm_client
                            else "deterministic"
                        ),
                        latency_ms=int(
                            (perf_counter() - start_time)
                            * 1000
                        ),
                        retry_count=retry_count,
                    ),
                    errors=[
                        AgentError(
                            error_type=ErrorType.SECURITY,
                            message=result.message,
                            retryable=False,
                        )
                    ],
                )

        #
        # Execute
        #

        try:

            payload = self.execute(
                request,
            )

        except Exception as ex:

            return AgentResponse(
                success=False,
                payload=None,
                metadata=AgentMetadata(
                    agent_name=self.agent_name,
                    model_name=(
                        self.llm_client.model_name
                        if self.llm_client
                        else "deterministic"
                    ),
                    latency_ms=int(
                        (perf_counter() - start_time)
                        * 1000
                    ),
                    retry_count=retry_count,
                ),
                errors=[
                    AgentError(
                        error_type=ErrorType.UNKNOWN,
                        message=str(ex),
                        retryable=True,
                    )
                ],
            )

        response = AgentResponse(
            success=True,
            payload=payload,
            metadata=AgentMetadata(
                agent_name=self.agent_name,
                model_name=(
                    self.llm_client.model_name
                    if self.llm_client
                    else "deterministic"
                ),
                latency_ms=int(
                    (perf_counter() - start_time)
                    * 1000
                ),
                retry_count=retry_count,
                confidence=1.0,
            ),
            errors=[],
        )

        validation_results = [
            validator.validate(
                response,
            )
            for validator in self.validators
        ]

        if self.recovery_agent.should_retry(
            validation_results,
            retry_count,
        ):

            return self.recovery_agent.recover(
                self,
                request,
                retry_count + 1,
            )

        response.metadata.validated = True

        return response