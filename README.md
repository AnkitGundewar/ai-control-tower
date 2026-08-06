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

- Shipment APIs
- AI Analysis APIs
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


                                   S3
                                   │
                                   ▼
                           Ingestion Lambda
                                   │
                                   ▼
                            DynamoDB Table
                                   │
                                   ▼
                                FastAPI
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

---
## Event-Driven Architecture

The AI Control Tower includes a fully serverless event-driven workflow that automatically analyzes shipment updates and notifies stakeholders without requiring any manual intervention.

The workflow begins when shipment data is uploaded to Amazon S3. An Ingestion Lambda processes the uploaded dataset and stores the shipment records in Amazon DynamoDB.

Every shipment record written to or modified in Amazon DynamoDB generates a DynamoDB Stream event. Since the Ingestion Lambda persists uploaded shipment data into DynamoDB, both newly ingested shipments and subsequent updates automatically enter the event-driven workflow. These events are forwarded to Amazon EventBridge Pipes, which filter and route only the relevant shipment updates to the Supervisor Lambda.

The Supervisor Lambda acts as the entry point into the AI orchestration layer. Rather than performing the analysis itself, it delegates execution to the **Supervisor**, which coordinates the specialized AI agents responsible for different aspects of shipment analysis.

The Supervisor invokes three independent analysis agents:

- **Tracking Agent** – Retrieves and structures shipment tracking information.
- **Risk Agent** – Evaluates shipment risk based on the available shipment context.
- **Root Cause Agent** – Determines the most likely operational cause affecting the shipment.

Once these analyses complete successfully, the **Recommendation Agent** combines their outputs to generate actionable recommendations for logistics operators.

Finally, the **Executive Summary Agent** synthesizes all preceding analyses into a concise operational summary suitable for business stakeholders.

After the AI workflow completes, the Supervisor Lambda asynchronously invokes the Notification Lambda. The Notification Lambda formats the executive summary into a notification and publishes it to an Amazon SNS topic. Amazon SNS then distributes the notification to all subscribed recipients via email.

This architecture enables shipment updates to be analyzed automatically as they occur, allowing stakeholders to receive AI-generated insights and recommendations without interacting directly with the dashboard application.

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
