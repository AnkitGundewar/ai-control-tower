from fastapi import APIRouter
from app.dependencies import (dashboard_service)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)

@router.get("/alerts")
def alerts():

    return dashboard_service.get_dashboard_alerts()


@router.get("/summary")
def summary():
    return dashboard_service.get_executive_summary()