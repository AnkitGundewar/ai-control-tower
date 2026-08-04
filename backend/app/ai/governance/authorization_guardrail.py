from app.ai.models.validation_result import (ValidationResult, Severity, RoutingDecision)
from app.ai.governance.base_guardrail import BaseGuardrail


class AuthorizationGuardrail(BaseGuardrail):

    ALLOWED_ROLES = {
        "administrator"
        "operator",
        "manager",
        "executive",
    }

    @property
    def guardrail_name(self):
        return "AuthorizationGuardrail"

    def validate(self, request):

        if request.user_role not in self.ALLOWED_ROLES:

            return ValidationResult(
                passed=False,
                validator=self.guardrail_name,
                severity=Severity.CRITICAL,
                message="Unauthorized role.",
                retryable=False,
                routing_decision=RoutingDecision.BLOCK,
            )

        return ValidationResult(
            passed=True,
            validator=self.guardrail_name,
        )