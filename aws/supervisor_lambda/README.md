# Supervisor Lambda - Testing

## Purpose

The Supervisor Lambda is responsible for triggering the AI Control Tower workflow whenever a shipment's metadata changes.

It is invoked by Amazon EventBridge after a DynamoDB Stream detects a modification to a shipment's `METADATA` record.


## Input

Example DynamoDB Stream record:

```json
{
  "eventName": "MODIFY",
  "dynamodb": {
    "Keys": {
      "PK": {
        "S": "SHIPMENT#SHP-20034"
      },
      "SK": {
        "S": "METADATA"
      }
    }
  }
}
