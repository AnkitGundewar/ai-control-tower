from app.ai.models.validation_result import ValidationResult
from app.ai.validators.base_validator import BaseValidator


class SchemaValidator(BaseValidator):

    @property
    def validator_name(self):
        return "SchemaValidator"

    def validate(self, response):

        if response.payload is None:

            return ValidationResult(
                passed=False,
                validator=self.validator_name,
                message="Payload is missing.",
                retryable=True,
            )

        return ValidationResult(
            passed=True,
            validator=self.validator_name,
        )