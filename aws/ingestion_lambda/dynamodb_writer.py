import boto3

from config import (
    AWS_REGION,
    CONTROL_TOWER_TABLE,
)

dynamodb = boto3.resource(
    "dynamodb",
    region_name=AWS_REGION,
)

table = dynamodb.Table(
    CONTROL_TOWER_TABLE,
)


def write_items(
    items: list[dict],
):

    with table.batch_writer() as batch:

        for item in items:

            batch.put_item(
                Item=item,
            )