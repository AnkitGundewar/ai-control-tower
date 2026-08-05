from app.repositories.dynamodb_control_tower_repository import DynamoDBControlTowerRepository

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

from app.ai.governance.authorization_guardrail import AuthorizationGuardrail
from app.ai.governance.security_guardrail import SecurityGuardrail
from app.ai.governance.prompt_injection_guardrail import PromptInjectionGuardrail
from app.ai.governance.pii_guardrail import PIIGuardrail
from app.ai.governance.token_limit_guardrail import TokenLimitGuardrail
from app.ai.governance.cost_guardrail import CostGuardrail

from app.ai.validators.schema_validator import SchemaValidator
from app.ai.validators.confidence_validator import ConfidenceValidator
from app.ai.validators.evidence_validator import EvidenceValidator
from app.ai.validators.hallucination_validator import HallucinationValidator

# ==========================================================
# Clients
# ==========================================================

llm_client = BedrockClient()
# llm_client = MockLLMClient()

# ==========================================================
# Repositories
# ==========================================================

control_tower_repository = (DynamoDBControlTowerRepository())

# ==========================================================
# Services
# ==========================================================

control_tower_service = (ControlTowerService(repository=control_tower_repository))
dashboard_service = DashboardService(control_tower_service=control_tower_service)

# ==========================================================
# Governance
# ==========================================================

common_guardrails = [
    AuthorizationGuardrail(),
    SecurityGuardrail(),
    PromptInjectionGuardrail(),
    PIIGuardrail(),
    TokenLimitGuardrail(),
    CostGuardrail(),
]

tracking_validators = [
    SchemaValidator(),
]
common_validators = [
    SchemaValidator(),
    ConfidenceValidator(),
    EvidenceValidator(),
    HallucinationValidator(),
]
# ==========================================================
# AI Agents
# ==========================================================

tracking_agent = TrackingAgent(
    control_tower_service=control_tower_service,
    llm_client=None,
    guardrails=common_guardrails,
    validators=tracking_validators,
)

risk_agent = RiskAgent(
    llm_client=llm_client,
    guardrails=common_guardrails,
    validators=common_validators,
)

root_cause_agent = RootCauseAgent(
    llm_client=llm_client,
    guardrails=common_guardrails,
    validators=common_validators,
)

recommendation_agent = RecommendationAgent(
    llm_client=llm_client,
    guardrails=common_guardrails,
    validators=common_validators,
)

executive_summary_agent = ExecutiveSummaryAgent(
    llm_client=llm_client,
    guardrails=common_guardrails,
    validators=common_validators,
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
    guardrails=common_guardrails,
    validators=common_validators,
)