from app.ai.agents.base_agent import BaseAgent
from app.ai.models.agent_request import AgentRequest
from app.ai.utils.prompt_loader import PromptLoader


class DashboardChatAgent(BaseAgent):

    def __init__(
        self,
        dashboard_service,
        *args,
        **kwargs,
    ):
        super().__init__(
            *args,
            **kwargs,
        )

        self.dashboard_service = (
            dashboard_service
        )

    @property
    def agent_name(
        self,
    ) -> str:
        return "Dashboard Chat Agent"

    def execute(
        self,
        request: AgentRequest,
    ) -> dict:

        question = request.payload.get(
            "question",
        )

        if question is None:

            raise ValueError(
                "Question not found in request payload."
            )

        dashboard_state = (
            self.dashboard_service.get_dashboard_state()
        )

        system_prompt = PromptLoader.load(
            "dashboard_ai_prompt.txt",
        )

        user_prompt = f"""
        User Question

        {question}

        Dashboard State

        {dashboard_state}

        Answer the user's question using ONLY the dashboard information.

        Do not invent shipment information.

        If information is unavailable, explicitly state that it is unavailable.

        Return ONLY valid JSON.
        """

        response = self.llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return response