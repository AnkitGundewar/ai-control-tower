from app.models.control_tower_context import ControlTowerContext, Shipment
from app.repositories.control_tower_repository import ControlTowerRepository

class ControlTowerService:
    def __init__(
        self,
        repository: ControlTowerRepository,
    ):
        self.repository = repository

    def get_context(
        self,
        shipment_id: str,
    ) -> ControlTowerContext | None:

        return self.repository.get_context(
            shipment_id,
        )

    def get_all_shipments(
        self,
    ) -> list[Shipment]:

        return self.repository.get_all_shipments()