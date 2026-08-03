from app.ai.models.validation_result import ValidationResult
from app.ai.validators.base_validator import BaseValidator

class EvidenceValidator(BaseValidator):
    @property
    def validator_name(self):
        return "EvidenceValidator"

    def validate(self, response):
        payload = response.payload or {}

        if "evidence" not in payload:

            return ValidationResult(
                passed = False,
                validator = self.validator_name,
                message="Evidence Missing.",
                retryable=True,
            )

        return ValidationResult(
            passed=True,
            validator=self.validator_name,
        )