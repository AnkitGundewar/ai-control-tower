from app.ai.models.validation_result import (ValidationResult, Severity, RoutingDecision)
from app.ai.governance.base_guardrail import BaseGuardrail

class CostGuardrail(BaseGuardrail):

    @property
    def guardrail_name(self):
        return "CostGuardrail"

    def validate(self, request):
        payload = str(request.payload).lower()
        deterministic_keywords = [
            "count",
            "total",
            "how many",
            "percentage",
        ]

        if any(keyword in payload for keyword in deterministic_keywords):
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