from datetime import datetime
from pydantic import BaseModel

class TokenUsage(BaseModel):
    input_tokens: int = 0
    output_tokens: int = 0

class AgentMetadata(BaseModel):
    agent_name: str
    model_name: str
    prompt_version: str = "v1"
    confidence: float = 1.0
    latency_ms: int = 0
    retry_count: int = 0
    validated: bool = False
    token_usage: TokenUsage = TokenUsage()
    timestamp: datetime = datetime.now(datetime.timezone.utc)()