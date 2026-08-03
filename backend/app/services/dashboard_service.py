from app.repositories.shipment_repository import ShipmentRepository

repository = ShipmentRepository()


def get_dashboard_alerts():
    shipments = repository.get_all_shipments()

    alerts = []

    for shipment in shipments:
        if shipment.status == "Delayed":
            alerts.append({
                "severity": "High",
                "title": f"{shipment.shipmentId} delayed",
                "description": shipment.delayReason,
            })

        elif shipment.slaRisk == "High":
            alerts.append({
                "severity": "Medium",
                "title": f"{shipment.shipmentId} at risk",
                "description": "Potential SLA breach.",
            })

    return alerts


def get_executive_summary():
    shipments = repository.get_all_shipments()

    total = len(shipments)

    delivered = len(
        [s for s in shipments if s.status == "Delivered"]
    )

    delayed = len(
        [s for s in shipments if s.status == "Delayed"]
    )

    at_risk = len(
        [s for s in shipments if s.status == "At Risk"]
    )

    in_transit = len(
        [s for s in shipments if s.status == "In Transit"]
    )

    return {
        "summary": (
            f"{total} shipments are currently being monitored. "
            f"{delivered} have been delivered successfully, "
            f"{in_transit} remain in transit, "
            f"{delayed} are delayed, "
            f"and {at_risk} are at risk of missing SLA."
        )
    }