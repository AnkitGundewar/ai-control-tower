from pydantic import BaseModel

class Shipment(BaseModel):
    shipmentId: str
    origin: str
    destination: str
    status : str
    carrier: str
    eta: str
    estRisk: str