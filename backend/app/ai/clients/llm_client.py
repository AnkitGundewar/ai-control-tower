from __future__ import annotations
from abc import ABC, abstractmethod

class LLMClient(ABC):
    """
    Abstract interface for every LLM provider.
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
    ) -> str:
        pass