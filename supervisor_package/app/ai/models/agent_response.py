from typing import Any
from pydantic import BaseModel
from app.ai.models.agent_error import AgentError
from app.ai.models.agent_metadata import AgentMetadata

class AgentResponse(BaseModel):
    success: bool
    payload: dict[str, Any] | None = None
    metadata: AgentMetadata
    errors: list[AgentError] = []