import json
import os

import boto3


class SNSClient:

    def __init__(self):

        self.client = boto3.client(
            "sns",
            region_name=os.environ["AWS_REGION"],
        )

        self.topic_arn = os.environ["SNS_TOPIC_ARN"]

    def publish(
        self,
        subject: str,
        message: str,
    ):

        self.client.publish(
            TopicArn=self.topic_arn,
            Subject=subject,
            Message=message,
        )