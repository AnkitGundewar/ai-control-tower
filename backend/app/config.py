from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    APP_NAME: str = "AI Control Tower"
    AWS_REGION: str = "us-east-1"
    AWS_PROFILE: str = "default"
    BEDROCK_MODEL_ID: str = (
        "anthropic.claude-sonnet-4-20250514-v1:0"
    )
    TEMPERATURE: float = 0.2
    MAX_TOKENS: int = 1500
    class Config:
        env_file = ".env"

settings = Settings()