from app.ai.agents.base_agent import BaseAgent
from app.ai.models.agent_request import AgentRequest
from app.ai.utils.prompt_loader import PromptLoader

class RiskAgent(BaseAgent):

    @property
    def agent_name(
        self,
    ) -> str:
        return "Risk Agent"

    def execute(
        self,
        request: AgentRequest,
    ) -> dict:

        tracking = request.payload["tracking"]

        shipment = tracking["shipment"]
        events = tracking["events"]

        system_prompt = PromptLoader.load("risk_prompt.txt")

        user_prompt = f"""
        Shipment Information

        Shipment ID: {shipment["shipmentId"]}
        Origin: {shipment["origin"]}
        Destination: {shipment["destination"]}
        Current Location: {shipment["currentLocation"]}
        Carrier: {shipment["carrier"]}
        Status: {shipment["status"]}
        ETA: {shipment["eta"]}
        SLA Deadline: {shipment.get("slaDeadline")}
        SLA Risk: {shipment["slaRisk"]}
        Delay Reason: {shipment.get("delayReason")}

        Shipment Events

        {events}

        Analyze the shipment risk using BOTH the shipment information and the shipment event history.

        Consider:

        - Shipment progress
        - Delay events
        - SLA risk
        - Timeline progression
        - Event sequence

        Return only valid JSON.
        """

        response = self.llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return {
            "shipmentId": shipment["shipmentId"],
            "riskAnalysis": response,
        }