from enum import Enum
from pydantic import BaseModel

class ErrorType(str, Enum):
    VALIDATION = "VALIDATION"
    HALLUCINATION = "HALLUCINATION"
    SECURITY = "SECURITY"
    PROMPT_INJECTION = "PROMPT_INJECTION"
    MODEL_ERROR = "MODEL_ERROR"
    TIMEOUT = "TIMEOUT"
    TOKEN_LIMIT = "TOKEN_LIMIT"
    UNKNOWN = "UNKNOWN"

class AgentError(BaseModel):
    error_type: ErrorType
    message: str
    retryable: bool = False