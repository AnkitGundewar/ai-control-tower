import json
import boto3

from s3_reader import read_events
from parser import parse_items
from validator import validate_items
from dynamodb_writer import write_items

s3 = boto3.client("s3")


def lambda_handler(
    event,
    context,
):

    record = event["Records"][0]

    bucket = (
        record["s3"]["bucket"]["name"]
    )

    key = (
        record["s3"]["object"]["key"]
    )

    file_contents = read_events(
        bucket,
        key,
    )

    items = parse_items(
        file_contents,
    )

    validated_items = validate_items(
        items,
    )

    write_items(
        validated_items,
    )

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "itemsWritten": len(
                    validated_items
                )
            }
        ),
    }