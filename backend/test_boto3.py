import boto3
import json

session = boto3.Session()
client = session.client("bedrock")

profiles = client.list_inference_profiles()

for profile in profiles["inferenceProfileSummaries"]:
    print("=" * 80)
    print("Name:", profile["inferenceProfileName"])
    print("ARN :", profile["inferenceProfileArn"])

    detail = client.get_inference_profile(
        inferenceProfileIdentifier=profile["inferenceProfileArn"]
    )

    print(json.dumps(detail["models"], indent=2))