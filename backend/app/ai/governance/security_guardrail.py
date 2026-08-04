from app.ai.governance.base_guardrail import BaseGuardrail
from app.ai.models.validation_result import ValidationResult


class SecurityGuardrail(BaseGuardrail):

    @property
    def guardrail_name(self):
        return "SecurityGuardrail"

    def validate(self, request):

        # Placeholder for future security policies

        return ValidationResult(
            passed=True,
            validator=self.guardrail_name,
        )