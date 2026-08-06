from app.ai.models.validation_result import (
    ValidationResult,
    Severity,
)

from app.ai.validators.base_validator import BaseValidator
from app.ai.models.agent_response import AgentResponse


class ConfidenceValidator(BaseValidator):

    MIN_CONFIDENCE = 0.70

    @property
    def validator_name(self) -> str:
        return "Confidence Validator"

    def validate(
        self,
        response: AgentResponse,
    ) -> ValidationResult:

        confidence = (
            response.metadata.confidence
            if response.metadata.confidence is not None
            else 0.0
        )

        if confidence < self.MIN_CONFIDENCE:

            return ValidationResult(
                passed=False,
                validator=self.validator_name,
                severity=Severity.WARNING,
                message=(
                    f"Confidence score "
                    f"({confidence:.2f}) is below the "
                    f"minimum threshold "
                    f"({self.MIN_CONFIDENCE:.2f})."
                ),
                retryable=True,
                metadata={
                    "confidence": confidence,
                    "minimum_confidence": self.MIN_CONFIDENCE,
                },
            )

        return ValidationResult(
            passed=True,
            validator=self.validator_name,
            severity=Severity.INFO,
            message="Confidence validation passed.",
            metadata={
                "confidence": confidence,
            },
        )