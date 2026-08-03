from app.ai.clients.llm_client import LLMClient

class MockLLMClient(LLMClient):
    @property
    def model_name(self) -> str:
        return "mock-llm"

    def generate(self, system_prompt: str, user_prompt: str) -> str :
        return """
        {"status": "SUCCESS"}
        """