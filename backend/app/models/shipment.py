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