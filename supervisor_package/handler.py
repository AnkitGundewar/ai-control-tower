import json
import logging
import os
import time
import uuid

import boto3

from app.dependencies import supervisor
from app.ai.models.agent_request import AgentRequest


logger = logging.getLogger()
logger.setLevel(logging.INFO)

lambda_client = boto3.client("lambda")


def _is_modify_event(record: dict) -> bool:
    return record.get("eventName") == "MODIFY"


def _is_metadata_record(record: dict) -> bool:
    try:
        return record["dynamodb"]["Keys"]["SK"]["S"] == "METADATA"
    except KeyError:
        return False


def _extract_shipment_id(record: dict) -> str:
    pk = record["dynamodb"]["Keys"]["PK"]["S"]

    if not pk.startswith("SHIPMENT#"):
        raise ValueError(f"Invalid PK: {pk}")

    return pk.replace("SHIPMENT#", "", 1)


def _invoke_notification_lambda(
    shipment_id: str,
    response: dict,
):
    """
    Fire-and-forget invocation of the Notification Lambda.
    """

    payload = {
        "shipmentId": shipment_id,
        "response": response,
    }

    lambda_client.invoke(
        FunctionName=os.environ["NOTIFICATION_LAMBDA_NAME"],
        InvocationType="Event",   # asynchronous
        Payload=json.dumps(payload).encode("utf-8"),
    )


def handler(event, context):

    start_time = time.perf_counter()

    #
    # Support both Lambda Console tests and EventBridge Pipes.
    #
    if isinstance(event, dict):
        records = event.get("Records", [event])

    elif isinstance(event, list):
        records = event

    else:
        raise ValueError(
            f"Unsupported event type: {type(event).__name__}"
        )

    logger.info("Received %d record(s).", len(records))

    results = []

    for index, record in enumerate(records):

        if not isinstance(record, dict):

            logger.warning(
                "Skipping non-dict record at index %d.",
                index,
            )
            continue

        logger.info(
            "Record %d | Event=%s | PK=%s",
            index,
            record.get("eventName"),
            record.get("dynamodb", {})
                  .get("Keys", {})
                  .get("PK", {})
                  .get("S"),
        )

        if not _is_modify_event(record):
            continue

        if not _is_metadata_record(record):
            continue

        shipment_id = _extract_shipment_id(record)

        logger.info(
            "Starting AI workflow for shipment %s.",
            shipment_id,
        )

        request = AgentRequest(
            request_id=str(uuid.uuid4()),
            correlation_id=str(uuid.uuid4()),
            session_id="eventbridge",
            user_role="admin",
            shipment_ids=[shipment_id],
            payload={},
        )

        try:

            response = supervisor.execute(request)

            logger.info(
                "AI workflow completed successfully for shipment %s.",
                shipment_id,
            )

            #
            # Invoke Notification Lambda asynchronously.
            #
            _invoke_notification_lambda(
                shipment_id=shipment_id,
                response=response,
            )

            logger.info(
                "Notification Lambda invoked for shipment %s.",
                shipment_id,
            )

            results.append(
                {
                    "shipmentId": shipment_id,
                    "response": response,
                }
            )

        except Exception:

            logger.exception(
                "AI workflow failed for shipment %s.",
                shipment_id,
            )

            #
            # Allow EventBridge Pipes to retry or send to DLQ.
            #
            raise

    elapsed = time.perf_counter() - start_time

    logger.info(
        "Processed %d shipment(s) in %.2f seconds.",
        len(results),
        elapsed,
    )

    return {
        "processed": len(results),
        "results": results,
    }