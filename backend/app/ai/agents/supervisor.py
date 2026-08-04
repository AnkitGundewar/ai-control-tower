from app.ai.models.agent_request import AgentRequest
from app.ai.agents.tracking_agent import TrackingAgent
from app.ai.agents.risk_agent import RiskAgent
from app.ai.agents.root_cause_agent import RootCauseAgent
from app.ai.agents.recommendation_agent import RecommendationAgent
from app.ai.agents.executive_summary_agent import ExecutiveSummaryAgent

class Supervisor:
    """
    Orchestrates the execution of all AI agents in the
    AI Control Tower workflow.
    """

    def __init__(
            self,
            tracking_agent: TrackingAgent,
            risk_agent: RiskAgent,
            root_cause_agent: RootCauseAgent,
            recommendation_agent: RecommendationAgent,
            executive_summary_agent: ExecutiveSummaryAgent,
        ):
        self.tracking_agent = tracking_agent
        self.risk_agent = risk_agent
        self.root_cause_agent = root_cause_agent
        self.recommendation_agent = recommendation_agent
        self.executive_summary_agent = executive_summary_agent

    def execute(self, request: AgentRequest) -> dict:
        # ------------------------------------
        # Tracking
        # ------------------------------------

        tracking_response = self.tracking_agent.run(request)
        if not tracking_response.success:
            return tracking_response

        # ------------------------------------
        # Risk
        # ------------------------------------

        risk_request = request.model_copy(deep=True)
        risk_request.payload["tracking"] = tracking_response.payload
        risk_response = self.risk_agent.run(risk_request)
        if not risk_response.success:
            return risk_response

        # ------------------------------------
        # Root Cause
        # ------------------------------------

        rca_request = request.model_copy(deep=True)
        rca_request.payload["tracking"] = tracking_response.payload
        rca_request.payload["riskAnalysis"] = risk_response.payload
        root_cause_response = self.root_cause_agent.run(rca_request)

        if not root_cause_response.success:
            return root_cause_response

        # ------------------------------------
        # Recommendation
        # ------------------------------------

        recommendation_request = request.model_copy(deep=True)
        recommendation_request.payload["tracking"] = tracking_response.payload
        recommendation_request.payload["riskAnalysis"] = risk_response.payload
        recommendation_request.payload["rootCauseAnalysis"] = root_cause_response.payload
        recommendation_response = self.recommendation_agent.run(recommendation_request)

        if not recommendation_response.success:
            return recommendation_response

        # ------------------------------------
        # Executive Summary
        # ------------------------------------

        summary_request = request.model_copy(deep=True)
        summary_request.payload["tracking"] = tracking_response.payload
        summary_request.payload["riskAnalysis"] = risk_response.payload
        summary_request.payload["rootCauseAnalysis"] = root_cause_response.payload
        summary_request.payload["recommendation"] = recommendation_response.payload
        executive_summary_response = self.executive_summary_agent.run(summary_request)

        if not executive_summary_response.success:
            return executive_summary_response

        return {
            "tracking": tracking_response.payload,
            "risk": risk_response.payload,
            "rootCause": root_cause_response.payload,
            "recommendation": recommendation_response.payload,
            "executiveSummary": executive_summary_response.payload,
        }