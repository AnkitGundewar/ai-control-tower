from fastapi import APIRouter, HTTPException

from app.dependencies import (
    control_tower_service,
)

router = APIRouter(
    prefix="/shipments",
    tags=["Shipments"],
)


@router.get("/")
def list_shipments():

    return control_tower_service.get_all_shipments()


@router.get("/{shipment_id}/context")
def shipment_context(
    shipment_id: str,
):

    context = control_tower_service.get_context(
        shipment_id,
    )

    if context is None:

        raise HTTPException(
            status_code=404,
            detail="Shipment not found.",
        )

    return context