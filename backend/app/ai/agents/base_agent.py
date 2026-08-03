from __future__ import annotations
from abc import ABC, abstractmethod
from time import perf_counter
from app.ai.models.agent_error import (AgentError,ErrorType)
from app.ai.models.agent_metadata import AgentMetadata
from app.ai.models.agent_request import AgentRequest
from app.ai.models.agent_response import AgentResponse

class BaseAgent(ABC):
    """
    Base class for every AI agent in the Control Tower.
    Every specialized agent inherits this class.
    """

    def __init__(self, llm_client):
        self.llm_client = llm_client
    @property
    @abstractmethod
    def agent_name(self) -> str:
        """Human-readable agent name."""
        pass

    @abstractmethod
    def execute(self, request: AgentRequest) -> dict:
        """
        Business logic implemented by the child agent.

        Should return ONLY the payload.
        """
        pass

    def run(self, request: AgentRequest) -> AgentResponse:
        """
        Standard execution pipeline shared by every AI agent.
        """

        start = perf_counter()

        try:
            payload = self.execute(request)

            metadata = AgentMetadata(
                agent_name=self.agent_name,
                model_name=self.llm_client.model_name,
                latency_ms=int((perf_counter() - start) * 1000),
                validated=False,
            )

            return AgentResponse(
                success=True,
                payload=payload,
                metadata=metadata,
                errors=[],
            )

        except Exception as ex:

            metadata = AgentMetadata(
                agent_name=self.agent_name,
                model_name=self.llm_client.model_name,
                latency_ms=int((perf_counter() - start) * 1000),
            )

            return AgentResponse(
                success=False,
                payload=None,
                metadata=metadata,
                errors=[
                    AgentError(
                        error_type=ErrorType.UNKNOWN,
                        message=str(ex),
                        retryable=True,
                    )
                ],
            )