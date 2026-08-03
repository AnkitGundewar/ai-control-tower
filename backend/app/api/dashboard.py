from fastapi import APIRouter

from app.services.dashboard_service import (
    get_dashboard_alerts,
    get_executive_summary,
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/alerts")
def alerts():
    return get_dashboard_alerts()


@router.get("/summary")
def summary():
    return get_executive_summary()