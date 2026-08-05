from app.ai.agents.base_agent import BaseAgent

from app.ai.models.agent_request import AgentRequest

from app.ai.utils.prompt_loader import PromptLoader


class ExecutiveSummaryAgent(BaseAgent):

    @property
    def agent_name(
        self,
    ) -> str:
        return "Executive Summary Agent"

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

        recommendation = request.payload[
            "recommendation"
        ]

        system_prompt = PromptLoader.load(
            "executive_summary_prompt.txt",
        )

        user_prompt = f"""
        Shipment Information

        Shipment ID: {shipment["shipmentId"]}
        Origin: {shipment["origin"]}
        Destination: {shipment["destination"]}
        Carrier: {shipment["carrier"]}
        Status: {shipment["status"]}
        Current Location: {shipment["currentLocation"]}
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

        Recommendation

        {recommendation}

        Generate a concise executive summary of the shipment, including:

        - Current shipment status
        - Overall risk
        - Primary root cause
        - Recommended actions
        - Overall business impact

        Return only valid JSON.
        """

        response = self.llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return {
            "shipmentId": shipment["shipmentId"],
            "executiveSummary": response,
        }