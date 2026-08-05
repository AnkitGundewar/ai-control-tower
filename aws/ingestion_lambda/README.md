# NovaMed Ingestion Lambda

This Lambda is triggered whenever a new shipment event file is uploaded to Amazon S3.

Responsibilities:

- Receive S3 ObjectCreated events
- Download shipment event JSON
- Parse shipment events
- Update DynamoDB
- Publish ShipmentUpdated event to Amazon EventBridge

This Lambda performs data ingestion only.

It does not perform AI analysis.