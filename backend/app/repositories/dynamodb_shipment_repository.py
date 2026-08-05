from app.models.shipment import Shipment
from app.repositories.shipment_repository import (ShipmentRepository)

from app.infrastructure.dynamodb_client import (DynamoDBClient)
from app.config import settings


class DynamoDBShipmentRepository(
    ShipmentRepository,
):

    def __init__(
        self,
    ):
        self.table = DynamoDBClient().get_table(
            settings.SHIPMENTS_TABLE,
        )

    def get_all_shipments(
        self,
    ) -> list[Shipment]:

        response = self.table.scan()

        items = response.get(
            "Items",
            [],
        )

        return [
            Shipment.model_validate(item)
            for item in items
        ]

    def get_shipment_by_id(
        self,
        shipment_id: str,
    ) -> Shipment | None:

        response = self.table.get_item(
            Key={
                "shipmentId": shipment_id,
            }
        )

        item = response.get(
            "Item",
        )

        if item is None:
            return None

        return Shipment.model_validate(
            item,
        )

    def get_events_for_shipment(
        self,
        shipment_id: str,
    ):
        raise NotImplementedError(
            "Events will be migrated in the next milestone."
        )