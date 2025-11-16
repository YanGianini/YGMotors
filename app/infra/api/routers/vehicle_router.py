from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infra.api.schemas.vehicle_dto import VehicleCreateRequest, VehicleResponse
from app.application.use_cases.create_vehicle import CreateVehicleUseCase
from app.infra.database.database import get_session
from app.infra.persistence.repositories.vehicle_repository_impl import VehicleRepositoryImpl

router = APIRouter(prefix="/vehicle", tags=["Vehicle"])

def get_vehicle_repository(session: AsyncSession = Depends(get_session)):
    return VehicleRepositoryImpl(session)

def get_create_vehicle_use_case(repo: VehicleRepositoryImpl = Depends(get_vehicle_repository)):
    return CreateVehicleUseCase(vehicle_repository=repo)


@router.post("/", response_model=VehicleResponse)
async def create_vehicle(
    payload: VehicleCreateRequest,
    use_case: CreateVehicleUseCase = Depends(get_create_vehicle_use_case)
):
    vehicle = await use_case.execute(
        brand=payload.brand,
        model=payload.model,
        year=payload.year,
        color=payload.color,
        price=payload.price
    )
    return vehicle
