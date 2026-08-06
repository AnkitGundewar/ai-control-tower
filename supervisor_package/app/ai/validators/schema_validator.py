from app.ai.models.agent_response import AgentResponse

from app.ai.models.validation_result import (
    ValidationResult,
    Severity,
)

from app.ai.validators.base_validator import BaseValidator


class SchemaValidator(BaseValidator):

    REQUIRED_FIELDS = {
        "Tracking Agent": [
            "shipment",
            "events",
        ],
        "Risk Agent": [
            "shipmentId",
            "riskAnalysis",
        ],
        "Root Cause Agent": [
            "shipmentId",
            "rootCauseAnalysis",
        ],
        "Recommendation Agent": [
            "shipmentId",
            "recommendation",
        ],
        "Executive Summary Agent": [
            "shipmentId",
            "executiveSummary",
        ],
        "Chat Agent": [
            "question",
            "answer",
        ],
    }

    @property
    def validator_name(self) -> str:
        return "Schema Validator"

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

        if not isinstance(payload, dict):

            return ValidationResult(
                passed=False,
                validator=self.validator_name,
                severity=Severity.ERROR,
                message="Response payload must be a dictionary.",
                retryable=True,
            )

        agent_name = response.metadata.agent_name

        required_fields = self.REQUIRED_FIELDS.get(
            agent_name,
            [],
        )

        missing_fields = [
            field
            for field in required_fields
            if field not in payload
        ]

        if missing_fields:

            return ValidationResult(
                passed=False,
                validator=self.validator_name,
                severity=Severity.ERROR,
                message=(
                    "Missing required fields: "
                    + ", ".join(missing_fields)
                ),
                retryable=True,
                metadata={
                    "missing_fields": missing_fields,
                },
            )

        return ValidationResult(
            passed=True,
            validator=self.validator_name,
            severity=Severity.INFO,
            message="Schema validation passed.",
        )