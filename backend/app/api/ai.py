from fastapi import APIRouter
from app.dependencies import (chat_agent, supervisor, dashboard_service, llm_client)
from app.ai.models.agent_request import AgentRequest
from app.ai.utils.prompt_loader import PromptLoader
router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/analyze")
def analyze(request: AgentRequest):
    return supervisor.execute(request)


@router.post("/chat")
def chat(request: AgentRequest):
    return chat_agent.run(request)

@router.post("/gchat")
def copilot(
    request: AgentRequest,
):

    question = request.payload.get(
        "question",
    )

    dashboard = (
        dashboard_service.get_dashboard_state()
    )

    system_prompt = PromptLoader.load(
        "dashboard_ai_prompt.txt",
    )

    user_prompt = f"""
User Question

{question}

Dashboard State

{dashboard}

Answer the user's question using ONLY the dashboard information.

Return only valid JSON.
"""

    return llm_client.generate(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
    )