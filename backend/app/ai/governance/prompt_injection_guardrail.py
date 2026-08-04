from app.ai.governance.base_guardrail import BaseGuardrail
from app.ai.models.validation_result import ValidationResult


class PromptInjectionGuardrail(BaseGuardrail):

    @property
    def guardrail_name(self):
        return "PromptInjectionGuardrail"

    def validate(self, request):

        # Placeholder for future prompt injection detection

        return ValidationResult(
            passed=True,
            validator=self.guardrail_name,
        )