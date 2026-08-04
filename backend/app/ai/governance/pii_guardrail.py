from app.ai.governance.base_guardrail import BaseGuardrail
from app.ai.models.validation_result import ValidationResult


class PIIGuardrail(BaseGuardrail):

    @property
    def guardrail_name(self):
        return "PIIGuardrail"

    def validate(self, request):

        # Placeholder for future PII detection

        return ValidationResult(
            passed=True,
            validator=self.guardrail_name,
        )