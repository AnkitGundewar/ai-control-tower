Hi there! Built out this AI Control Tower Dashboard over the past few days and it was a tedious job. So I am not going to go much into details 
and simply give you small commands to run different aspects of this project in your local machine.


# Setup
---


Just clone this repository as it is and I'll give terminal commands from there. 

P.S.: This project uses Amazon services but if you're just building the dashboard - You only require a DynamoDB table (or a local dataset repository) and any model from Amazon Bedrock. I have used "anthropic.claude-sonnet-4-6" but you can choose whichever model you want.


### Backend
---
If you're running this locally and just want a backend for your dashboard and nothing more than that. 
From the project root:

cd backend

<strong> set up your .venv (For packages) and .env (For environment variables) </strong>

pip install -r requirements.txt

uvicorn app.main:app --reload

Click on the link/docs (http://127.0.0.1:8000/docs) and you can test and debug different backend features. 


### Frontend
---
Rejoice. You don't have to deal with a virtual environment here. From project root:

cd frontend 

npm create vite@latest . -- --template react 

npm install

npm run dev

(http://localhost:5173)

Now it should ideally give you a loading page with a circular loader and you are on the right track. The dashboard utilizes a bunch of AI and non-AI features so bear with me. 

- KPI Card: To indicate total, delayed, high-risk, on time KPIs for shipments in the dataset. 
- Executive summary - AI summary of all the shipments in the dataset
- Global AI Chat - To answer any questions you might have regarding generic shipments. (Eg. Which shipments should I prioritize?)
- Operational Alerts - Lists all the hazards the shipments in your dataset are going through
- Search bar - Allows you to actively search using any of the mentioned criteria (Shipment ID, Origin, Destination, Carrier Service, Status)
- Dashboard Grid: Lists all the shipments in your dataset with some information for the dashboard

Now if you click on a shipment:
Dashboard Drawer - Gives you information about the selected shipment. Such as:
  - Shipment Timeline - Order of events leading up to current status of shipment
  - AI Analyze - Gives an AI analysis about the current condition of the shipment: with Risk, Root Cause Analysis, Recommendation action going forward and a summary of information collected about the shipment.
  - Shipment AI - Can answer any questions pertaining to the selected shipment. (Eg. Why is my shipment delayed? What caused the delay? By when can I expect delivery? etc.)

