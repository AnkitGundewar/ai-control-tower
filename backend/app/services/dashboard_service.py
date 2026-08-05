from app.ai.models.agent_request import AgentRequest
from app.services.control_tower_service import (
    ControlTowerService,
)
from app.ai.agents.dashboard_summary_agent import (
    DashboardSummaryAgent,
)


class DashboardService:

    def __init__(
        self,
        control_tower_service: ControlTowerService,
        dashboard_summary_agent: DashboardSummaryAgent,
    ):
        self.control_tower_service = (
            control_tower_service
        )

        self.dashboard_summary_agent = (
            dashboard_summary_agent
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

    def get_dashboard_context(
        self,
    ) -> dict:

        shipments = (
            self.control_tower_service.get_all_shipments()
        )

        return {
            "shipments": [
                shipment.model_dump()
                for shipment in shipments
            ]
        }

    def get_executive_summary(
        self,
    ) -> dict:

        request = AgentRequest(
            request_id="dashboard-summary",
            correlation_id="dashboard-summary",
            session_id="dashboard-summary",
            user_role="operator",
            shipment_ids=[],
            payload={
                "dashboardContext": (
                    self.get_dashboard_context()
                )
            },
        )

        response = (
            self.dashboard_summary_agent.run(
                request,
            )
        )

        if not response.success:

            raise RuntimeError(
                response.errors[0].message
            )

        return response.payload

    def get_dashboard_state(
        self,
    ) -> dict:

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
            "summary": (
                self.get_executive_summary()[
                    "summary"
                ]
            ),
            "shipments":[
                shipment.model_dump()
                for shipment in shipments
            ]
        }