from fastapi import APIRouter, HTTPException

from app.services.shipment_service import (
    get_all_shipments,
    get_shipment_by_id,
    get_events_for_shipment,
)

router = APIRouter(
    prefix="/shipments",
    tags=["Shipments"],
)


@router.get("/")
def list_shipments():
    return get_all_shipments()


@router.get("/{shipment_id}")
def shipment_details(shipment_id: str):

    shipment = get_shipment_by_id(shipment_id)

    if shipment is None:
        raise HTTPException(
            status_code=404,
            detail="Shipment not found",
        )

    return shipment


@router.get("/{shipment_id}/events")
def shipment_events(shipment_id: str):

    shipment = get_shipment_by_id(shipment_id)

    if shipment is None:
        raise HTTPException(
            status_code=404,
            detail="Shipment not found",
        )

    return get_events_for_shipment(shipment_id)