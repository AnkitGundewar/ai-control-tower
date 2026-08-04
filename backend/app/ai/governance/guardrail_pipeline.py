from app.ai.models.agent_request import AgentRequest
from app.ai.models.validation_result import ValidationResult

class GuardrailPipeline:
    def __init__(self, guardrails):
        self.guardrails = guardrails

    def validate(
        self,
        request: AgentRequest,
    ) -> list[ValidationResult]:

        results = []
        for guardrail in self.guardrails:
            results.append(
                guardrail.validate(request)
            )
        return results