import boto3
from botocore.exceptions import (
    BotoCoreError,
    ClientError,
)

from app.ai.clients.llm_client import LLMClient
from app.ai.exceptions.llm_exception import LLMException
from app.ai.parsers.json_response_parser import JsonResponseParser

from app.config import settings


class BedrockClient(LLMClient):

    def __init__(self):

        session = boto3.Session(
            profile_name=settings.AWS_PROFILE,
            region_name=settings.AWS_REGION,
        )

        self.client = session.client(
            "bedrock-runtime",
        )

    @property
    def model_name(self):
        return settings.BEDROCK_MODEL_ID

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> dict:

        try:

            response = self.client.converse(
                modelId=settings.BEDROCK_MODEL_ID,
                system=[
                    {
                        "text": system_prompt,
                    }
                ],
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": user_prompt,
                            }
                        ],
                    }
                ],
                inferenceConfig={
                    "temperature": settings.TEMPERATURE,
                    "maxTokens": settings.MAX_TOKENS,
                },
                additionalModelRequestFields={
                    "top_k": 250,
                },
                performanceConfig={
                    "latency": "standard",
                },
            )

            usage = response.get(
                "usage",
                {},
            )

            input_tokens = usage.get(
                "inputTokens",
                0,
            )

            output_tokens = usage.get(
                "outputTokens",
                0,
            )

        except (
            ClientError,
            BotoCoreError,
        ) as ex:

            raise LLMException(
                str(ex)
            ) from ex

        try:

            text = response["output"]["message"]["content"][0]["text"]

        except (
            KeyError,
            IndexError,
        ) as ex:

            raise LLMException(
                "Invalid Bedrock response."
            ) from ex

        # print("=" * 80)
        # print(text)
        # print("=" * 80)


        return JsonResponseParser.parse(text)