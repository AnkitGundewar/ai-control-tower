from abc import ABC, abstractmethod

from app.ai.models.agent_request import AgentRequest
from app.ai.models.validation_result import ValidationResult


class BaseGuardrail(ABC):
    """
    Base class for all request guardrails.
    Every guardrail validates an incoming AgentRequest
    before an agent executes.
    """

    @property
    @abstractmethod
    def guardrail_name(self) -> str:
        """
        Human-readable guardrail name.
        """
        raise NotImplementedError

    @abstractmethod
    def validate(
        self,
        request: AgentRequest,
    ) -> ValidationResult:
        """
        Validate an incoming request.

        Returns:
            ValidationResult
        """
        raise NotImplementedError