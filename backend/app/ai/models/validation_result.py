from enum import Enum
from pydantic import BaseModel, Field

class Severity(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class RoutingDecision(str, Enum):
    LLM = "LLM"
    DETERMINISTIC = "DETERMINISTIC"
    CACHE = "CACHE"
    BLOCK = "BLOCK"

class ValidationResult(BaseModel):
    passed: bool
    validator: str
    severity: Severity = Severity.ERROR
    message: str = ""
    retryable: bool = False
    routing_decision: RoutingDecision | None = None
    metadata: dict = Field(default_factory=dict)