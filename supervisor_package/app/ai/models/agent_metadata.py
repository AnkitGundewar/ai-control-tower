from datetime import datetime, timezone
from pydantic import BaseModel, Field

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
    token_usage: TokenUsage = Field(default_factory=TokenUsage,)

    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc,),)