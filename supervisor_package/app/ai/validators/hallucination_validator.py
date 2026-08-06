from app.ai.models.agent_response import AgentResponse

from app.ai.models.validation_result import (
    ValidationResult,
    Severity,
)

from app.ai.validators.base_validator import BaseValidator


class HallucinationValidator(BaseValidator):

    BLOCKED_PHRASES = [
        "based on historical data",
        "historical trends",
        "weather conditions",
        "traffic conditions",
        "port congestion",
        "labor strike",
        "supplier issue",
        "news reports",
        "market conditions",
        "economic conditions",
        "social media",
        "internet search",
        "external data",
        "public records",
    ]

    @property
    def validator_name(self) -> str:
        return "Hallucination Validator"

    def validate(
        self,
        response: AgentResponse,
    ) -> ValidationResult:

        payload = response.payload

        if payload is None:

            return ValidationResult(
                passed=False,
                validator=self.validator_name,
                severity=Severity.ERROR,
                message="Response payload is missing.",
                retryable=True,
            )

        text = str(payload).lower()

        for phrase in self.BLOCKED_PHRASES:

            if phrase in text:

                return ValidationResult(
                    passed=False,
                    validator=self.validator_name,
                    severity=Severity.WARNING,
                    message=(
                        f"Potential hallucination detected: '{phrase}'."
                    ),
                    retryable=True,
                    metadata={
                        "matched_phrase": phrase,
                    },
                )

        return ValidationResult(
            passed=True,
            validator=self.validator_name,
            severity=Severity.INFO,
            message="Hallucination validation passed.",
        )