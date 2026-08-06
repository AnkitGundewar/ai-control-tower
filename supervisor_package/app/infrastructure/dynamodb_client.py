import boto3
from app.config import settings

class DynamoDBClient:
    def __init__(self):
        session = boto3.Session(
            profile_name=settings.AWS_PROFILE,
            region_name=settings.AWS_REGION,
        )

        self.resource = session.resource(
            "dynamodb",
        )

    def get_table(
        self,
        table_name: str,
    ):
        return self.resource.Table(table_name)