import json
from pathlib import Path

import boto3

from app.config import settings

from app.models.shipment import Shipment
from app.models.shipment_event import ShipmentEvent


def main():

    session = boto3.Session(
        profile_name=settings.AWS_PROFILE,
        region_name=settings.AWS_REGION,
    )

    table = session.resource(
        "dynamodb",
    ).Table(
        settings.CONTROL_TOWER_TABLE,
    )

    project_root = Path(__file__).resolve().parents[2]

    shipments_file = (
        project_root
        / "sample-data"
        / "shipments.json"
    )

    events_file = (
        project_root
        / "sample-data"
        / "shipment_events.json"
    )

    with open(
        shipments_file,
        encoding="utf-8",
    ) as file:

        shipments = json.load(file)

    with open(
        events_file,
        encoding="utf-8",
    ) as file:

        events = json.load(file)

    print(
        f"Loading {len(shipments)} shipments..."
    )

    print(
        f"Loading {len(events)} shipment events..."
    )

    with table.batch_writer() as batch:

        #
        # Shipment metadata
        #
        for item in shipments:

            shipment = Shipment.model_validate(
                item,
            )

            batch.put_item(
                Item={
                    "PK": f"SHIPMENT#{shipment.shipmentId}",
                    "SK": "METADATA",
                    **shipment.model_dump(),
                }
            )

        #
        # Shipment events
        #
        for item in events:

            event = ShipmentEvent.model_validate(
                item,
            )

            batch.put_item(
                Item={
                    "PK": f"SHIPMENT#{event.shipmentId}",
                    "SK": f"EVENT#{event.timestamp}",
                    **event.model_dump(),
                }
            )

    print("Done.")


if __name__ == "__main__":
    main()