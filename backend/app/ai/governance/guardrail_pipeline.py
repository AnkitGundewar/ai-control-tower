from app.ai.governance.base_guardrail import BaseGuardrail

from app.ai.models.agent_request import AgentRequest
from app.ai.models.validation_result import ValidationResult


class GuardrailPipeline:

    def __init__(
        self,
        guardrails: list[BaseGuardrail],
    ):
        self.guardrails = guardrails

    def validate(
        self,
        request: AgentRequest,
    ) -> list[ValidationResult]:

        validation_results: list[ValidationResult] = []

        for guardrail in self.guardrails:

            validation_results.append(
                guardrail.validate(
                    request,
                )
            )

        return validation_results