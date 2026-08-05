from app.ai.governance.base_guardrail import BaseGuardrail
from app.ai.models.agent_request import AgentRequest
from app.ai.models.validation_result import (
    ValidationResult,
    Severity,
    RoutingDecision,
)


class CostGuardrail(BaseGuardrail):

    MAX_CHARACTERS = 20000

    @property
    def guardrail_name(self) -> str:
        return "Cost Guardrail"

    def validate(
        self,
        request: AgentRequest,
    ) -> ValidationResult:

        payload = str(request.payload)
        payload_lower = payload.lower()

        if len(payload) > self.MAX_CHARACTERS:
            return ValidationResult(
                passed=False,
                validator=self.guardrail_name,
                severity=Severity.ERROR,
                routing_decision=RoutingDecision.BLOCK,
                retryable=False,
                message="Request exceeds maximum allowed size.",
                metadata={
                    "payload_length": len(payload),
                },
            )

        deterministic_keywords = [
            "count",
            "total",
            "how many",
            "percentage",
            "average",
            "sum",
            "max",
            "min",
        ]

        if any(
            keyword in payload_lower
            for keyword in deterministic_keywords
        ):
            return ValidationResult(
                passed=True,
                validator=self.guardrail_name,
                severity=Severity.INFO,
                routing_decision=RoutingDecision.DETERMINISTIC,
                message="Deterministic execution recommended.",
            )

        return ValidationResult(
            passed=True,
            validator=self.guardrail_name,
            severity=Severity.INFO,
            routing_decision=RoutingDecision.LLM,
            message="LLM execution approved.",
        )