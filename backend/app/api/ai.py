from fastapi import APIRouter, HTTPException

from app.ai.agents.supervisor import Supervisor
from app.ai.agents.chat_agent import ChatAgent
from app.ai.agents.tracking_agent import TrackingAgent
from app.ai.agents.risk_agent import RiskAgent
from app.ai.agents.root_cause_agent import RootCauseAgent
from app.ai.agents.recommendation_agent import RecommendationAgent
from app.ai.agents.executive_summary_agent import ExecutiveSummaryAgent

from app.ai.clients.mock_llm_client import MockLLMClient

from app.ai.models.agent_request import AgentRequest

router = APIRouter(prefix="/ai", tags=["AI"])

llm_client = MockLLMClient()

tracking_agent = TrackingAgent(llm_client=None, guardrails=[], validators=[])
risk_agent = RiskAgent(llm_client=llm_client, guardrails=[], validators=[])
root_cause_agent = RootCauseAgent(llm_client=llm_client, guardrails=[], validators=[])
recommendation_agent = RecommendationAgent(llm_client=llm_client, guardrails=[], validators=[])
executive_summary_agent = ExecutiveSummaryAgent( llm_client=llm_client, guardrails=[], validators=[],)

supervisor = Supervisor(
    tracking_agent=tracking_agent,
    risk_agent=risk_agent,
    root_cause_agent=root_cause_agent,
    recommendation_agent=recommendation_agent,
    executive_summary_agent=executive_summary_agent,
)

chat_agent = ChatAgent(supervisor=supervisor, llm_client=llm_client, guardrails=[], validators=[])

@router.post("/analyze")
def analyze(
    request: AgentRequest,
):
    return supervisor.execute(request)


@router.post("/chat")
def chat(
    request: AgentRequest,
):
    return chat_agent.run(request)