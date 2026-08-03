from pydantic import BaseModel

class ValidationResult(BaseModel):
    passed: bool
    validator: str
    message: str = ""
    retryable: bool = False