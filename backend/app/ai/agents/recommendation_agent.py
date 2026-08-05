from app.ai.agents.base_agent import BaseAgent

from app.ai.models.agent_request import AgentRequest

from app.ai.utils.prompt_loader import PromptLoader


class RecommendationAgent(BaseAgent):

    @property
    def agent_name(
        self,
    ) -> str:
        return "Recommendation Agent"

    def execute(
        self,
        request: AgentRequest,
    ) -> dict:

        tracking = request.payload["tracking"]

        shipment = tracking["shipment"]
        events = tracking["events"]

        risk_analysis = request.payload[
            "riskAnalysis"
        ]

        root_cause_analysis = request.payload[
            "rootCauseAnalysis"
        ]

        system_prompt = PromptLoader.load(
            "recommendation_prompt.txt",
        )

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

        Risk Analysis

        {risk_analysis}

        Root Cause Analysis

        {root_cause_analysis}

        Based on the shipment information, shipment event history, risk analysis, and root cause analysis, recommend the best corrective actions.

        Return only valid JSON.
        """

        response = self.llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return {
            "shipmentId": shipment["shipmentId"],
            "recommendation": response,
        }