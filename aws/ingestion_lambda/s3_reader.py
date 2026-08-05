import boto3

s3 = boto3.client("s3")


def read_events(
    bucket: str,
    key: str,
) -> str:

    response = s3.get_object(
        Bucket=bucket,
        Key=key,
    )

    return (
        response["Body"]
        .read()
        .decode("utf-8")
    )