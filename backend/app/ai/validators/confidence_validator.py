from app.ai.models.validation_result import ValidationResult
from app.ai.validators.base_validator import BaseValidator

class ConfidenceValidator(BaseValidator):

    MIN_CONFIDENCE = 0.70

    @property
    def validator_name(self):
        return "ConfidenceValidator"
    
    def validate(self, response):
        confidence = response.metadata.confidence
        
        if confidence < self.MIN_CONFIDENCE:
            return ValidationResult(
                passed=False,
                validator=self.validator_name,
                message=(
                    f"Confidence "
                    f"{confidence:.2f} "
                    f"is below threshold."
                ),
                retryable=True,
            )
        return ValidationResult(
            passed=True,
            validator=self.validator_name,
        )