from app.models.shipment import Shipment
from app.models.shipment_event import ShipmentEvent

from app.repositories.shipment_repository import ShipmentRepository


class ShipmentService:

    def __init__(
        self,
        shipment_repository: ShipmentRepository,
    ):
        self.shipment_repository = shipment_repository

    def get_all_shipments(
        self,
    ) -> list[Shipment]:

        return self.shipment_repository.get_all_shipments()

    def get_shipment_by_id(
        self,
        shipment_id: str,
    ) -> Shipment | None:

        return self.shipment_repository.get_shipment_by_id(
            shipment_id,
        )

    def get_events_for_shipment(
        self,
        shipment_id: str,
    ) -> list[ShipmentEvent]:

        return self.shipment_repository.get_events_for_shipment(
            shipment_id,
        )