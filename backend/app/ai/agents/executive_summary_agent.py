from app.ai.agents.base_agent import BaseAgent
from app.ai.models.agent_request import AgentRequest
from app.ai.utils.prompt_loader import PromptLoader

class ExecutiveSummaryAgent(BaseAgent):
    @property
    def agent_name(self) -> str:
        return "Executive Summary Agent"

    def execute(
        self,
        request: AgentRequest,
    ) -> dict:
        risk_analysis = request.payload.get("riskAnalysis")
        root_cause_analysis = request.payload.get("rootCauseAnalysis")
        recommendation = request.payload.get("recommendation")

        shipment = self.get_shipment(request)
        system_prompt = PromptLoader.load("executive_summary_prompt.txt")
        user_prompt = f"""
        Shipment ID: {shipment.shipmentId}
        Status: {shipment.status}
        Current Location: {shipment.currentLocation}
        ETA: {shipment.eta}
        Risk Analysis:{risk_analysis}
        Root Cause Analysis:{root_cause_analysis}
        Recommendation:{recommendation}
        """

        response = self.llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return {
            "shipmentId": shipment.shipmentId,
            "executiveSummary": response,
        }