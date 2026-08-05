from pydantic import BaseModel

from app.models.shipment import Shipment
from app.models.shipment_event import ShipmentEvent


class ControlTowerContext(BaseModel):
    shipment: Shipment
    events: list[ShipmentEvent]