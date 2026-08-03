from typing import Any
from pydantic import BaseModel

class AgentRequest(BaseModel):
    request_id: str
    correlation_id: str
    session_id: str | None = None
    user_role: str = "operator"
    shipment_ids: list[str] = []
    payload: dict[str, Any]