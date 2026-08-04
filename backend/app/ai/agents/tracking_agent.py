from app.ai.agents.base_agent import BaseAgent
from app.ai.models.agent_request import AgentRequest


class TrackingAgent(BaseAgent):

    @property
    def agent_name(self) -> str:
        return "Tracking Agent"

    def execute(
        self,
        request: AgentRequest,
    ) -> dict:

        shipment = self.get_shipment(request)

        return {
            "shipmentId": shipment.shipmentId,
            "origin": shipment.origin,
            "destination": shipment.destination,
            "carrier": shipment.carrier,
            "status": shipment.status,
            "currentLocation": shipment.currentLocation,
            "eta": shipment.eta,
            "slaRisk": shipment.slaRisk,
        }