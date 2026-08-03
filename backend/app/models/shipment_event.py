from pydantic import BaseModel

class ShipmentEvent(BaseModel):
    shipmentId: str
    timestamp: str
    location: str
    eventType: str
    details: str