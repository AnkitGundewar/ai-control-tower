from fastapi import APIRouter
from app.dependencies import (chat_agent, supervisor)
from app.ai.models.agent_request import AgentRequest

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/analyze")
def analyze(request: AgentRequest):
    return supervisor.execute(request)


@router.post("/chat")
def chat(request: AgentRequest):
    return chat_agent.run(request)