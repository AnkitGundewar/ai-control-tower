from app.ai.agents.base_agent import BaseAgent
from app.ai.models.agent_request import AgentRequest
from app.ai.utils.prompt_loader import PromptLoader


class DashboardSummaryAgent(BaseAgent):

    @property
    def agent_name(
        self,
    ) -> str:
        return "Dashboard Summary Agent"

    def execute(
        self,
        request: AgentRequest,
    ) -> dict:

        dashboard_context = request.payload.get(
            "dashboardContext",
        )

        if dashboard_context is None:

            raise ValueError(
                "Dashboard context not found."
            )

        system_prompt = PromptLoader.load(
            "dashboard_summary_prompt.txt",
        )

        user_prompt = f"""
        Dashboard Context

        {dashboard_context}

        Generate an executive summary for supply chain leadership.

        Use ONLY the dashboard context provided.

        Return ONLY valid JSON.
        """

        response = self.llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return response