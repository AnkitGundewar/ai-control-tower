from abc import ABC, abstractmethod

from app.models.control_tower_context import ControlTowerContext
from app.models.shipment import Shipment

class ControlTowerRepository(ABC):

    @abstractmethod
    def get_context(
        self,
        shipment_id: str,
    ) -> ControlTowerContext | None:
        pass

    @abstractmethod
    def get_all_shipments(
        self,
    ) -> list[Shipment]:
        pass