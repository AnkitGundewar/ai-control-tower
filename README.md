# AI Control Tower

An AI-powered supply chain monitoring platform that combines a React dashboard, FastAPI backend, and a multi-agent AI orchestration system to analyze shipment health, identify operational risks, determine root causes, generate recommendations, and proactively notify stakeholders through an event-driven AWS architecture.

## Features

- Interactive shipment dashboard
- AI-powered shipment analysis
- Executive summaries
- Shipment AI assistant
- Dashboard AI assistant
- Multi-agent orchestration
- Event-driven monitoring
- Automated email notifications
- Serverless AWS deployment

# 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/AnkitGundewar/ai-control-tower.git
cd ai-control-tower
```

---

# Prerequisites

Before running the application, ensure you have:

- Python 3.13+
- Node.js 20+
- npm
- AWS Account
- Amazon Bedrock model access
- Amazon DynamoDB table
- Amazon S3 bucket (optional, if using the ingestion workflow)

The backend uses Amazon Bedrock for AI inference. This project was developed using:

```
anthropic.claude-sonnet-4-6
```

although any supported Bedrock model can be configured.

---

# Backend

Navigate to the backend:

```bash
cd backend
```

Create and activate a virtual environment.

macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and configure the required environment variables.

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Swagger documentation will be available at:

```
http://127.0.0.1:8000/docs
```

The backend provides:

- Shipment Management APIs
- Shipment AI Analysis APIs
- Executive Summary APIs
- Dashboard APIs
- AI Chat APIs

---

# Frontend

Navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The application will be available at:

```
http://localhost:5173
```

After the frontend loads, the dashboard provides:

### Dashboard Overview

- KPI cards summarizing shipment health
- Executive AI Summary
- Operational Alerts
- Global AI Chat
- Shipment Search
- Shipment Grid

### Shipment Details

Selecting a shipment opens a detailed drawer containing:

- Shipment Timeline
- AI Analysis
- Risk Assessment
- Root Cause Analysis
- Recommended Actions
- Executive Summary
- Shipment-specific AI Chat

# Application Architecture

Shipment datasets are uploaded to Amazon S3 and ingested into DynamoDB through an AWS Lambda function. The dashboard consumes this centralized data source through the FastAPI backend while the same dataset also powers the event-driven monitoring workflow.


                              Amazon S3
                                   │
                                   ▼
                           Ingestion Lambda
                                   │
                                   ▼
                         Amazon DynamoDB Table
                                   │
                                   ▼
                            FastAPI Backend
                                   │
                                   ▼
                             Supervisor
                                   │
      ┌────────────────────────────┼────────────────────────────┐
      │                            │                            │
      ▼                            ▼                            ▼         
      Tracking Agent              Risk Agent               Root Cause Agent
      │                            │                            │
      └────────────────────────────┴┬───────────────────────────┘
                                    │                         
                                    ▼                         
                           Recommendation Agent
                                    │
                                    ▼
                          Executive Summary Agent
                                    │
                        ┌───────────┴───────────┐
                        │                       │
                        ▼                       ▼
               Shipment AI Agent        Executive Summary
                        │                       │
                        └───────────┬───────────┘
                                    ▼
                         React Dashboard Components

### AI Workflow Design

The AI workflow follows a modular orchestration pattern where each agent has a single, well-defined responsibility. Rather than relying on a single large prompt to perform every analytical task, the system delegates specific responsibilities to specialized AI agents.

Each agent focuses exclusively on its designated task—tracking, risk assessment, root cause analysis, recommendation generation, executive summarization, or conversational assistance. This modular design improves maintainability, enables individual prompts to evolve independently, and produces structured outputs that can be reused across multiple application workflows.

The Supervisor coordinates these specialized agents, ensuring that analytical context is progressively enriched while keeping each agent isolated from responsibilities outside its domain.

### Key Design Principles

- **Single Responsibility:** Each AI agent performs one specialized analytical task.
- **Modular Orchestration:** The Supervisor coordinates agent execution while keeping individual agents focused on their own responsibility.
- **Structured AI Outputs:** Every agent produces structured JSON responses that can be consumed by downstream application components.
- **Separation of Concerns:** Business orchestration is handled by the Supervisor, while individual agents are responsible only for their specific analytical task.
- **Reusable AI Components:** The same AI orchestration layer is used by both the interactive dashboard and the autonomous event-driven workflow.

---
## Event-Driven Architecture

The AI Control Tower includes a fully serverless event-driven workflow that automatically analyzes shipment updates and notifies stakeholders without requiring any manual intervention.

The workflow begins when shipment data is uploaded to Amazon S3. An Ingestion Lambda processes the uploaded dataset and stores the shipment records in Amazon DynamoDB.

Every shipment record written to or modified in Amazon DynamoDB generates a DynamoDB Stream event. 

Since the Ingestion Lambda persists uploaded shipment data into DynamoDB, both newly ingested shipments and subsequent updates automatically enter the event-driven workflow. These events are forwarded to Amazon EventBridge Pipes, which filter and route only the relevant shipment updates to the Supervisor Lambda.

The Supervisor Lambda serves as the entry point into the AI orchestration layer. It initializes the **Supervisor**, which coordinates the execution of specialized AI agents responsible for shipment analysis.

The Supervisor orchestrates the AI workflow by coordinating three specialized analysis agents, each responsible for evaluating a different aspect of the shipment:

- **Tracking Agent** – Retrieves and structures shipment tracking information.
- **Risk Agent** – Evaluates shipment risk based on the available shipment context.
- **Root Cause Agent** – Determines the most likely operational cause affecting the shipment.

After the tracking, risk, and root cause analyses complete, the **Recommendation Agent** combines their outputs to generate actionable recommendations for logistics operators.

Finally, the **Executive Summary Agent** consolidates the outputs of the preceding agents into a concise, executive-level summary suitable for operational stakeholders and downstream notification services.

After the AI workflow completes, the Supervisor Lambda asynchronously invokes the Notification Lambda. The Notification Lambda formats the executive summary into a notification and publishes it to an Amazon SNS topic. Amazon SNS then distributes the notification to all subscribed recipients via email.

This architecture enables shipment updates to be analyzed automatically as they occur, allowing shipment events to be analyzed and communicated automatically without requiring users to manually initiate the AI workflow through the dashboard.

### Workflow

                           Amazon S3
                                │
                                ▼
                       Ingestion Lambda
                                │
                                ▼
                       Amazon DynamoDB
                                │
                                ▼
                      DynamoDB Streams
                                │
                                ▼
                    Amazon EventBridge Pipe
                                │
                                ▼
                     Supervisor Lambda
                                │
                                ▼
    ┌──────────────────────────────────────────────────────────────┐
    │                        Supervisor                            │
    │                                                              │
    │  Tracking ──┐                                                │
    │             ├──► Recommendation ─► Executive Summary         │
    │  Risk ──────┤                                                │
    │             │                                                │
    │  Root Cause ┘                                                │
    └──────────────────────────────────────────────────────────────┘
                                │
                                ▼
                    Notification Lambda
                                │
                                ▼
                         Amazon SNS
                                │
                                ▼
                    Email Notification Subscription


This architecture demonstrates two complementary execution models within the AI Control Tower:

- **Interactive AI**, where users request analyses through the dashboard.
- **Event-driven AI**, where shipment updates automatically trigger autonomous analysis and stakeholder notifications.

Together, these workflows provide both on-demand operational intelligence and proactive monitoring capabilities while sharing a common AI orchestration layer.