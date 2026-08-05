from app.ai.governance.base_guardrail import BaseGuardrail
from app.ai.models.agent_request import AgentRequest
from app.ai.models.validation_result import (
    ValidationResult,
    Severity,
    RoutingDecision,
)


class SecurityGuardrail(BaseGuardrail):

    BLOCKED_PATTERNS = [
        "<script",
        "</script>",
        "javascript:",
        "onerror=",
        "onload=",
        "eval(",
        "exec(",
        "__import__",
        "subprocess",
        "os.system",
        "rm -rf",
        "drop table",
        "truncate table",
        "delete from",
        "union select",
        "--",
        "/*",
        "*/",
        "../",
        "..\\",
        "/etc/passwd",
        "cmd.exe",
        "powershell",
        "bash -c",
    ]

    @property
    def guardrail_name(self) -> str:
        return "Security Guardrail"

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
                    message=f"Potential security threat detected: '{pattern}'.",
                    metadata={
                        "matched_pattern": pattern,
                    },
                )

        return ValidationResult(
            passed=True,
            validator=self.guardrail_name,
            severity=Severity.INFO,
            routing_decision=RoutingDecision.LLM,
            message="Security validation passed.",
        )