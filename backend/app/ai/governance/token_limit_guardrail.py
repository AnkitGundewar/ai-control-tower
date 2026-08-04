from app.ai.models.validation_result import (ValidationResult, Severity, RoutingDecision)
from app.ai.governance.base_guardrail import BaseGuardrail

class TokenLimitGuardrail(BaseGuardrail):
    MAX_INPUT_CHARS = 8000

    @property
    def guardrail_name(self):
        return "TokenLimitGuardrail"

    def validate(self, request):
        prompt_size = len(str(request.payload))

        if prompt_size > self.MAX_INPUT_CHARS:
            return ValidationResult(
                passed=False,
                validator=self.guardrail_name,
                severity=Severity.ERROR,
                message="Prompt exceeds allowed size.",
                retryable=False,
                routing_decision=RoutingDecision.BLOCK,
            )

        return ValidationResult(
            passed=True,
            validator=self.guardrail_name,
        )