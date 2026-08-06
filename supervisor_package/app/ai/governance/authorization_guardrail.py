from app.ai.governance.base_guardrail import BaseGuardrail
from app.ai.models.agent_request import AgentRequest
from app.ai.models.validation_result import (
    ValidationResult,
    Severity,
    RoutingDecision,
)


class AuthorizationGuardrail(BaseGuardrail):

    ALLOWED_ROLES = {
        "operator",
        "manager",
        "executive",
        "admin",
        "system"
    }

    @property
    def guardrail_name(self) -> str:
        return "Authorization Guardrail"

    def validate(
        self,
        request: AgentRequest,
    ) -> ValidationResult:

        role = (request.user_role or "").lower().strip()

        if role not in self.ALLOWED_ROLES:
            return ValidationResult(
                passed=False,
                validator=self.guardrail_name,
                severity=Severity.CRITICAL,
                message=f"Unauthorized role: {role}",
                retryable=False,
                routing_decision=RoutingDecision.BLOCK,
            )

        return ValidationResult(
            passed=True,
            validator=self.guardrail_name,
        )