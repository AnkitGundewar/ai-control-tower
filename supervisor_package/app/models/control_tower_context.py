from pydantic import BaseModel

class Shipment(BaseModel):
    shipmentId: str
    origin: str
    destination: str
    carrier: str
    status: str
    currentLocation: str
    eta: str
    slaDeadline: str
    slaRisk: str
    delayReason: str

class ShipmentEvent(BaseModel):
    shipmentId: str
    timestamp: str
    location: str
    eventType: str
    details: str
class ControlTowerContext(BaseModel):
    shipment: Shipment
    events: list[ShipmentEvent]