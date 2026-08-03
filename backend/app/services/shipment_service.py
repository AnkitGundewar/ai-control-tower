from app.repositories.shipment_repository import ShipmentRepository


repository = ShipmentRepository()


def get_all_shipments():
    return repository.get_all_shipments()


def get_shipment_by_id(shipment_id: str):
    return repository.get_shipment_by_id(shipment_id)

def get_events_for_shipment(shipment_id: str):
    return repository.get_events_for_shipment(shipment_id)