# Supervisor Lambda

## Purpose

The Supervisor Lambda is responsible for triggering the AI Control Tower workflow whenever a shipment's metadata changes.

It is invoked by Amazon EventBridge after a DynamoDB Stream detects a modification to a shipment's `METADATA` record.

---

## Responsibilities

- Receive shipment update events
- Filter supported DynamoDB events
- Extract the shipment ID
- Build an `AgentRequest`
- Invoke the Control Tower Supervisor
- Return the workflow result

---

## Dependencies

The Supervisor Lambda uses the shared backend dependencies defined in:

backend/requirements.txt

No separate dependency file is maintained for this Lambda.

---

## Workflow

DynamoDB
↓
DynamoDB Streams
↓
EventBridge Pipe
↓
Supervisor Lambda
↓
Supervisor.execute()
↓
Tracking Agent
↓
Risk Agent
↓
Root Cause Agent
↓
Recommendation Agent
↓
Executive Summary Agent

---

## Event Source

Amazon DynamoDB Streams

The Lambda processes only:

- MODIFY events
- Records where `SK == METADATA`

Timeline (`EVENT#...`) records are ignored.

---

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