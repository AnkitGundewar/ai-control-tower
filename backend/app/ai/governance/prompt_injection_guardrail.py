from app.ai.governance.base_guardrail import BaseGuardrail
from app.ai.models.agent_request import AgentRequest
from app.ai.models.validation_result import (
    ValidationResult,
    Severity,
    RoutingDecision,
)


class PromptInjectionGuardrail(BaseGuardrail):

    BLOCKED_PATTERNS = [
        "ignore previous instructions",
        "ignore all previous instructions",
        "forget previous instructions",
        "forget your instructions",
        "system prompt",
        "developer prompt",
        "developer message",
        "reveal your prompt",
        "show your prompt",
        "print your prompt",
        "repeat your instructions",
        "act as",
        "pretend to be",
        "jailbreak",
        "bypass",
        "disable guardrails",
        "ignore guardrails",
        "override instructions",
        "new instructions",
        "you are now",
    ]

    @property
    def guardrail_name(self) -> str:
        return "Prompt Injection Guardrail"

    def validate(
        self,
        request: AgentRequest,
    ) -> ValidationResult:

        payload = str(request.payload).lower()

        for pattern in self.BLOCKED_PATTERNS:

            if pattern in payload:

                return ValidationResult(
                    passed=False,
                    validator=self.guardrail_name,
                    severity=Severity.CRITICAL,
                    retryable=False,
                    routing_decision=RoutingDecision.BLOCK,
                    message=f"Potential prompt injection detected: '{pattern}'.",
                    metadata={
                        "matched_pattern": pattern,
                    },
                )

        return ValidationResult(
            passed=True,
            validator=self.guardrail_name,
            severity=Severity.INFO,
            routing_decision=RoutingDecision.LLM,
            message="No prompt injection detected.",
        )