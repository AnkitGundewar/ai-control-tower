from abc import ABC, abstractmethod

from app.models.shipment import Shipment
from app.models.shipment_event import ShipmentEvent


class ShipmentRepository(ABC):

    @abstractmethod
    def get_all_shipments(self) -> list[Shipment]:
        pass

    @abstractmethod
    def get_shipment_by_id(
        self,
        shipment_id: str,
    ) -> Shipment | None:
        pass

    @abstractmethod
    def get_events_for_shipment(
        self,
        shipment_id: str,
    ) -> list[ShipmentEvent]:
        pass