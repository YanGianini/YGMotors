from app.domain.models.vehicle_status import VehicleStatusEnum
from pydantic import BaseModel, Field


class VehicleCreateRequest(BaseModel):
    brand: str = Field(..., example="Toyota")
    model: str = Field(..., example="Corolla")
    year: int = Field(..., example=2018)
    color: str = Field(..., example="Prata")
    price: float = Field(..., example=45000.00)


class VehicleResponse(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    color: str
    price: float
    status: VehicleStatusEnum

    class Config:
        from_attributes = True
