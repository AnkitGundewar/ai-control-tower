from boto3.dynamodb.conditions import Key

from app.config import settings
from app.infrastructure.dynamodb_client import DynamoDBClient

from app.models.control_tower_context import ControlTowerContext
from app.models.shipment import Shipment
from app.models.shipment_event import ShipmentEvent

from app.repositories.control_tower_repository import (
    ControlTowerRepository,
)


class DynamoDBControlTowerRepository(
    ControlTowerRepository,
):

    def __init__(
        self,
    ):
        self.table = DynamoDBClient().get_table(
            settings.CONTROL_TOWER_TABLE,
        )

    @staticmethod
    def _clean_item(
        item: dict,
    ) -> dict:

        item = dict(item)

        item.pop("PK", None)
        item.pop("SK", None)
        item.pop("entityType", None)

        return item

    def get_context(
        self,
        shipment_id: str,
    ) -> ControlTowerContext | None:

        response = self.table.query(
            KeyConditionExpression=Key("PK").eq(
                f"SHIPMENT#{shipment_id}"
            )
        )

        items = response.get(
            "Items",
            [],
        )

        if not items:
            return None

        shipment = None
        events = []

        for item in items:

            if item["SK"] == "METADATA":

                shipment = Shipment.model_validate(
                    self._clean_item(item)
                )

            elif item["SK"].startswith("EVENT#"):

                events.append(
                    ShipmentEvent.model_validate(
                        self._clean_item(item)
                    )
                )

        if shipment is None:
            return None

        events.sort(
            key=lambda event: event.timestamp
        )

        return ControlTowerContext(
            shipment=shipment,
            events=events,
        )

    def get_all_shipments(
        self,
    ) -> list[Shipment]:

        response = self.table.scan()

        shipments = []

        for item in response.get(
            "Items",
            [],
        ):

            if item["SK"] != "METADATA":
                continue

            shipments.append(
                Shipment.model_validate(
                    self._clean_item(item)
                )
            )

        return shipments