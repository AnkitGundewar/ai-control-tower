from abc import ABC, abstractmethod

from app.ai.models.agent_response import AgentResponse
from app.ai.models.validation_result import ValidationResult


class BaseValidator(ABC):
    """
    Base class for all response validators.

    Validators execute after an agent completes and before the
    response is returned to the caller.
    """

    @property
    @abstractmethod
    def validator_name(self) -> str:
        """
        Human-readable validator name.
        """
        raise NotImplementedError

    @abstractmethod
    def validate(
        self,
        response: AgentResponse,
    ) -> ValidationResult:
        """
        Validate an agent response.

        Returns:
            ValidationResult
        """
        raise NotImplementedError