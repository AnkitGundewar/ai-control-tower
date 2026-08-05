import re

from app.ai.governance.base_guardrail import BaseGuardrail
from app.ai.models.agent_request import AgentRequest
from app.ai.models.validation_result import (
    ValidationResult,
    Severity,
    RoutingDecision,
)


class PIIGuardrail(BaseGuardrail):

    EMAIL_PATTERN = re.compile(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    )

    PHONE_PATTERN = re.compile(
        r"\b(?:\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    )

    SSN_PATTERN = re.compile(
        r"\b\d{3}-\d{2}-\d{4}\b"
    )

    CREDIT_CARD_PATTERN = re.compile(
        r"\b(?:\d[ -]*?){13,16}\b"
    )

    @property
    def guardrail_name(self) -> str:
        return "PII Guardrail"

    def validate(
        self,
        request: AgentRequest,
    ) -> ValidationResult:

        payload = str(request.payload)

        patterns = [
            ("email", self.EMAIL_PATTERN),
            ("phone", self.PHONE_PATTERN),
            ("ssn", self.SSN_PATTERN),
            ("credit_card", self.CREDIT_CARD_PATTERN),
        ]

        for pii_type, pattern in patterns:

            if pattern.search(payload):

                return ValidationResult(
                    passed=False,
                    validator=self.guardrail_name,
                    severity=Severity.CRITICAL,
                    retryable=False,
                    routing_decision=RoutingDecision.BLOCK,
                    message=f"Detected {pii_type} in request.",
                    metadata={
                        "pii_type": pii_type,
                    },
                )

        return ValidationResult(
            passed=True,
            validator=self.guardrail_name,
            severity=Severity.INFO,
            message="No PII detected.",
        )