from app.ai.models.agent_request import AgentRequest
from app.ai.models.agent_response import AgentResponse
from app.ai.models.validation_result import ValidationResult

class RecoveryAgent:
    MAX_RETRIES = 1
    def should_retry(
        self,
        validation_results: list[ValidationResult],
        retry_count: int,
    ) -> bool:
        if retry_count >= self.MAX_RETRIES:
            return False

        return any(
            not result.passed and result.retryable
            for result in validation_results
        )

    def recover(
        self,
        agent,
        request: AgentRequest,
        retry_count: int,
    ) -> AgentResponse:
        """
        Retry the complete execution pipeline exactly once.
        """

        return agent._run_pipeline(
            request=request,
            retry_count=retry_count,
        )