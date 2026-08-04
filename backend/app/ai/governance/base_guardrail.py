from abc import ABC, abstractmethod
from app.ai.models.agent_request import AgentRequest
from app.ai.models.validation_result import ValidationResult

class BaseGuardrail(ABC):
    """
    Base class for every input guardrail.
    """

    @property
    @abstractmethod
    def guardrail_name(self) -> str:
        pass

    @abstractmethod
    def validate(
        self,
        request: AgentRequest,
    ) -> ValidationResult:
        pass