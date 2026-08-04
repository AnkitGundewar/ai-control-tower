from app.ai.agents.base_agent import BaseAgent
from app.ai.models.agent_request import AgentRequest
from app.ai.utils.prompt_loader import PromptLoader

class ChatAgent(BaseAgent):
    def __init__(
        self,
        supervisor,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.supervisor = supervisor

    @property
    def agent_name(self) -> str:
        return "Chat Agent"

    def execute(
        self,
        request: AgentRequest,
    ) -> dict:

        question = request.payload.get("question")

        if question is None:
            raise ValueError(
                "Question not found in request payload."
            )

        workflow_result = self.supervisor.execute(
            request,
        )

        system_prompt = PromptLoader.load("chat_prompt.txt")
        user_prompt = f"""
User Question:
{question}

Workflow Results:
{workflow_result}

Respond to the user's question using ONLY the workflow results.
"""

        response = self.llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return response