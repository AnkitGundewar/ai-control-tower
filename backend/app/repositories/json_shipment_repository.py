import json
from pathlib import Path

from app.models.shipment import Shipment
from app.models.shipment_event import ShipmentEvent

from app.repositories.shipment_repository import ShipmentRepository


class JsonShipmentRepository(
    ShipmentRepository,
):

    def __init__(self):

        project_root = Path(__file__).resolve().parents[3]

        self.shipments_file = (
            project_root
            / "sample-data"
            / "shipments.json"
        )

        self.events_file = (
            project_root
            / "sample-data"
            / "shipment_events.json"
        )

    def get_all_shipments(self) -> list[Shipment]:

        with open(self.shipments_file) as file:
            data = json.load(file)

        return [
            Shipment(**shipment)
            for shipment in data
        ]

    def get_shipment_by_id(self, shipment_id: str) -> Shipment | None:

        for shipment in self.get_all_shipments():

            if shipment.shipmentId == shipment_id:
                return shipment

        return None

    def get_events_for_shipment(self, shipment_id: str) -> list[ShipmentEvent]:

        with open(self.events_file) as file:
            data = json.load(file)

        events = [
            ShipmentEvent(**event)
            for event in data
            if event["shipmentId"] == shipment_id
        ]

        events.sort(
            key=lambda event: event.timestamp
        )

        return events