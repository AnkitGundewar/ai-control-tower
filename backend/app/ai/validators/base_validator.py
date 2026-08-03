from abc import ABC, abstractmethod
from app.ai.models.agent_response import AgentResponse
from app.ai.models.validation_result import ValidationResult

class BaseValidator(ABC):
    """
    Base class for every validator.
    """
    @property
    @abstractmethod
    def validator_name(self) -> str:
        pass

    @abstractmethod
    def validate(
        self,
        response: AgentResponse,
    ) -> ValidationResult:
        pass