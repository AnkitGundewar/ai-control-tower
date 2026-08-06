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
