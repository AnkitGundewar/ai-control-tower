# from app.repositories.json_shipment_repository import (JsonShipmentRepository)
# from app.repositories.dynamodb_shipment_repository import (DynamoDBShipmentRepository)
from app.repositories.dynamodb_control_tower_repository import DynamoDBControlTowerRepository

# from app.services.shipment_service import (ShipmentService)
from app.services.control_tower_service import  ControlTowerService
from app.services.dashboard_service import (DashboardService)

from app.ai.clients.bedrock_client import (BedrockClient)
# from app.ai.clients.mock_llm_client import (MockLLMClient)

from app.ai.agents.chat_agent import (ChatAgent)
from app.ai.agents.tracking_agent import (TrackingAgent)
from app.ai.agents.risk_agent import (RiskAgent)
from app.ai.agents.root_cause_agent import (RootCauseAgent)
from app.ai.agents.recommendation_agent import (RecommendationAgent)
from app.ai.agents.executive_summary_agent import (ExecutiveSummaryAgent)
from app.ai.agents.supervisor import (Supervisor)


# ==========================================================
# Repositories
# ==========================================================

# shipment_repository = JsonShipmentRepository()
# shipment_repository = DynamoDBShipmentRepository()
control_tower_repository = (DynamoDBControlTowerRepository())
control_tower_service = (ControlTowerService(repository=control_tower_repository))

# ==========================================================
# Services
# ==========================================================

# shipment_service = ShipmentService(shipment_repository=shipment_repository)
# dashboard_service = DashboardService(shipment_repository=shipment_repository)
dashboard_service = DashboardService(control_tower_service=control_tower_service)
# ==========================================================
# AI Agents
# ==========================================================

llm_client = BedrockClient()
# llm_client = MockLLMClient()

tracking_agent = TrackingAgent(
    control_tower_service=control_tower_service,
    llm_client=None,
    guardrails=[],
    validators=[],
)

risk_agent = RiskAgent(
    llm_client=llm_client,
    guardrails=[],
    validators=[],
)

root_cause_agent = RootCauseAgent(
    llm_client=llm_client,
    guardrails=[],
    validators=[],
)

recommendation_agent = RecommendationAgent(
    llm_client=llm_client,
    guardrails=[],
    validators=[],
)

executive_summary_agent = ExecutiveSummaryAgent(
    llm_client=llm_client,
    guardrails=[],
    validators=[],
)

supervisor = Supervisor(
    tracking_agent=tracking_agent,
    risk_agent=risk_agent,
    root_cause_agent=root_cause_agent,
    recommendation_agent=recommendation_agent,
    executive_summary_agent=executive_summary_agent,
)

chat_agent = ChatAgent(
    supervisor=supervisor,
    llm_client=llm_client,
    guardrails=[],
    validators=[],
)