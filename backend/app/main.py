from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.shipments import router as shipment_router

app = FastAPI(
    title="NovaMed AI Control Tower",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(shipment_router)

@app.get("/")
def home():
    return {
        "message": "NovaMed AI Control Tower API is running"
    }