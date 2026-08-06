from abc import ABC, abstractmethod

class LLMClient(ABC):
    """
    Base interface for all LLM providers.

    Every implementation MUST return a Python dictionary.
    Implementations are responsible for parsing any JSON
    returned by the underlying model.
    """

    @property
    @abstractmethod
    def model_name(self) -> str:
        pass

    @abstractmethod
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> dict:
        """
        Executes an LLM request and returns
        a structured Python dictionary.
        """
        pass