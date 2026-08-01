from app.models.shipment import Shipment

shipments = [
    Shipment(
        shipmentId="SHP-20034",
        origin="Boston",
        destination="London",
        status="In Transit",
        carrier="FedEx",
        eta="2026-08-03T15:00:00Z",
        estRisk="Low",
    ),
    Shipment(
            shipmentId="SHP-20035",
            origin="New York",
            destination="Mumbai",
            status="Delayed",
            carrier="DHL",
            eta="2026-08-07T09:00:00Z",
            estRisk="High",
        ),
]

def get_all_shipments():
    return shipments

def get_shipment_by_id(shipment_id: str):
    for shipment in shipments:
        if shipment.shipmentId == shipment_id:
            return shipment

    return None