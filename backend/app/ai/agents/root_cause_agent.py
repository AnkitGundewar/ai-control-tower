from app.ai.agents.base_agent import BaseAgent
from app.ai.models.agent_request import AgentRequest
from app.ai.utils.prompt_loader import PromptLoader

class RootCauseAgent(BaseAgent):
    @property
    def agent_name(self) -> str:
        return "Root Cause Agent"

    def execute(
        self,
        request: AgentRequest,
    ) -> dict:

        risk_analysis = request.payload.get("riskAnalysis")
        
        shipment = self.get_shipment(request)
        system_prompt = PromptLoader.load("root_cause_prompt.txt")
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
        """

        response = self.llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return {
            "shipmentId": shipment.shipmentId,
            "rootCauseAnalysis": response,
        }