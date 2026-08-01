from fastapi import FastAPI
from app.api.shipments import router as shipment_router

app = FastAPI(
    title="NovaMed AI Control Tower",
    version="1.0.0"
)

app.include_router(shipment_router)

@app.get("/")
def home():
    return {
        "message": "NovaMed AI Control Tower API is running"
    }