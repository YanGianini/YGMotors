from fastapi import FastAPI
from app.infra.api.routers.sale_router import router as sale_router
from app.infra.api.routers.vehicle_router import router as vehicle_router

app = FastAPI(title="YG Motors API", version="1.0.0")
app.include_router(vehicle_router)
app.include_router(sale_router)

@app.get("/health")
async def healthcheck():
    return {"status": "ok"}
