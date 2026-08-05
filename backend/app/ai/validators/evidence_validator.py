from app.ai.models.agent_response import AgentResponse

from app.ai.models.validation_result import (
    ValidationResult,
    Severity,
)

from app.ai.validators.base_validator import BaseValidator


class EvidenceValidator(BaseValidator):

    @property
    def validator_name(self) -> str:
        return "Evidence Validator"

    def validate(
        self,
        response: AgentResponse,
    ) -> ValidationResult:

        payload = response.payload or {}

        evidence = None

        if isinstance(payload, dict):

            if "evidence" in payload:

                evidence = payload.get(
                    "evidence",
                )

            else:

                for value in payload.values():

                    if (
                        isinstance(value, dict)
                        and "evidence" in value
                    ):
                        evidence = value.get(
                            "evidence",
                        )
                        break

        if (
            evidence is None
            or not isinstance(
                evidence,
                list,
            )
            or len(evidence) == 0
        ):

            return ValidationResult(
                passed=False,
                validator=self.validator_name,
                severity=Severity.WARNING,
                message="Evidence is missing from the response.",
                retryable=True,
            )

        return ValidationResult(
            passed=True,
            validator=self.validator_name,
            severity=Severity.INFO,
            message="Evidence validation passed.",
            metadata={
                "evidence_count": len(evidence),
            },
        )