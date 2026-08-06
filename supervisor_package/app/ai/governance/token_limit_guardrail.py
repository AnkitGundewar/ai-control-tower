from app.ai.governance.base_guardrail import BaseGuardrail
from app.ai.models.agent_request import AgentRequest
from app.ai.models.validation_result import (
    ValidationResult,
    Severity,
    RoutingDecision,
)


class TokenLimitGuardrail(BaseGuardrail):

    MAX_INPUT_CHARS = 8000

    @property
    def guardrail_name(self) -> str:
        return "Token Limit Guardrail"

    def validate(
        self,
        request: AgentRequest,
    ) -> ValidationResult:

        prompt = str(request.payload)
        prompt_size = len(prompt)

        if prompt_size > self.MAX_INPUT_CHARS:

            return ValidationResult(
                passed=False,
                validator=self.guardrail_name,
                severity=Severity.ERROR,
                retryable=False,
                routing_decision=RoutingDecision.BLOCK,
                message=(
                    f"Prompt exceeds maximum allowed size "
                    f"({prompt_size} > {self.MAX_INPUT_CHARS} characters)."
                ),
                metadata={
                    "prompt_size": prompt_size,
                    "max_size": self.MAX_INPUT_CHARS,
                },
            )

        return ValidationResult(
            passed=True,
            validator=self.guardrail_name,
            severity=Severity.INFO,
            routing_decision=RoutingDecision.LLM,
            message="Prompt size is within the allowed limit.",
            metadata={
                "prompt_size": prompt_size,
            },
        )