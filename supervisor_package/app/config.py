from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Control Tower"
    AWS_REGION: str = "us-east-1"
    # Optional.
    # Local Development:
    #   AWS_PROFILE=default
    #
    # Lambda:
    #   Leave unset so Lambda uses its execution role.
    AWS_PROFILE: str | None = None
    CONTROL_TOWER_TABLE: str
    BEDROCK_MODEL_ID: str
    TEMPERATURE: float = 0.2
    MAX_TOKENS: int = 1500
    class Config:
        env_file = ".env"
settings = Settings()