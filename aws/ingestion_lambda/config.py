import os

# ==========================================================
# AWS Configuration
# ==========================================================

AWS_REGION = os.getenv(
    "AWS_REGION",
    "us-east-1",
)

# ==========================================================
# DynamoDB
# ==========================================================

CONTROL_TOWER_TABLE = os.getenv(
    "CONTROL_TOWER_TABLE",
    "ControlTower",
)

# ==========================================================
# EventBridge
# ==========================================================

EVENT_BUS_NAME = os.getenv(
    "EVENT_BUS_NAME",
    "default",
)

EVENT_SOURCE = "novamed.controltower"

EVENT_DETAIL_TYPE = "ShipmentUpdated"