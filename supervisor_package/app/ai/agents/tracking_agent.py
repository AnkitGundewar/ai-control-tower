from app.ai.agents.base_agent import BaseAgent
from app.ai.models.agent_request import AgentRequest
from app.services.control_tower_service import (ControlTowerService)

class TrackingAgent(BaseAgent):
    def __init__(
        self,
        control_tower_service: ControlTowerService,
        *args,
        **kwargs,
    ):
        super().__init__(
            *args,
            **kwargs,
        )

        self.control_tower_service = (
            control_tower_service
        )

    @property
    def agent_name(
        self,
    ) -> str:
        return "Tracking Agent"

    def execute(
        self,
        request: AgentRequest,
    ) -> dict:

        shipment_id = request.shipment_ids[0]

        context = (
            self.control_tower_service.get_context(
                shipment_id,
            )
        )

        if context is None:
            raise ValueError(
                f"Shipment '{shipment_id}' not found."
            )

        return context.model_dump()