from app.ai.agents.base_agent import BaseAgent
from app.ai.models.agent_request import AgentRequest
from app.ai.utils.prompt_loader import PromptLoader

class RecommendationAgent(BaseAgent):

    @property
    def agent_name(self) -> str:
        return "Recommendation Agent"

    def execute(
        self,
        request: AgentRequest,
    ) -> dict:

        risk_analysis = request.payload.get("riskAnalysis")
        root_cause_analysis = request.payload.get("rootCauseAnalysis")

        shipment = self.get_shipment(request)
        system_prompt = PromptLoader.load("recommendation_prompt.txt")
        user_prompt = f"""
        Shipment ID: {shipment.shipmentId}
        Origin: {shipment.origin}
        Destination: {shipment.destination}
        Current Location: {shipment.currentLocation}
        Carrier: {shipment.carrier}
        Status: {shipment.status}
        ETA: {shipment.eta}
        SLA Risk: {shipment.slaRisk}
        Risk Analysis:{risk_analysis}
        Root Cause Analysis:{root_cause_analysis}
        """

        response = self.llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return {
            "shipmentId": shipment.shipmentId,
            "recommendation": response,
        }