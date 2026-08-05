from app.services.control_tower_service import (ControlTowerService)

class DashboardService:

    def __init__(
        self,
        control_tower_service: ControlTowerService,
    ):
        self.control_tower_service = (
            control_tower_service
        )

    def get_dashboard_alerts(
        self,
    ) -> list[dict]:

        shipments = (
            self.control_tower_service.get_all_shipments()
        )

        alerts = []

        for shipment in shipments:

            if shipment.status == "Delayed":

                alerts.append(
                    {
                        "severity": "High",
                        "title": f"{shipment.shipmentId} delayed",
                        "description": shipment.delayReason,
                    }
                )

            elif shipment.slaRisk == "High":

                alerts.append(
                    {
                        "severity": "Medium",
                        "title": f"{shipment.shipmentId} at risk",
                        "description": "Potential SLA breach.",
                    }
                )

        return alerts

    def get_executive_summary(
        self,
    ) -> dict:

        shipments = (
            self.control_tower_service.get_all_shipments()
        )

        total = len(shipments)

        delivered = len(
            [
                shipment
                for shipment in shipments
                if shipment.status == "Delivered"
            ]
        )

        delayed = len(
            [
                shipment
                for shipment in shipments
                if shipment.status == "Delayed"
            ]
        )

        at_risk = len(
            [
                shipment
                for shipment in shipments
                if shipment.status == "At Risk"
            ]
        )

        in_transit = len(
            [
                shipment
                for shipment in shipments
                if shipment.status == "In Transit"
            ]
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

    def get_dashboard_state(self) -> dict:

        shipments = (
            self.control_tower_service.get_all_shipments()
        )

        total = len(shipments)

        delayed = len(
            [
                shipment
                for shipment in shipments
                if shipment.status == "Delayed"
            ]
        )

        high_risk = len(
            [
                shipment
                for shipment in shipments
                if shipment.slaRisk == "High"
            ]
        )

        on_time = (
            0
            if total == 0
            else round(
                ((total - delayed) / total) * 100,
                1,
            )
        )

        return {
            "metrics": {
                "total": total,
                "delayed": delayed,
                "highRisk": high_risk,
                "onTime": on_time,
            },
            "alerts": self.get_dashboard_alerts(),
            "summary": self.get_executive_summary()["summary"],
        }