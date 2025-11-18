from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.application.use_cases.edit_vehicle import UpdateVehicleUseCase
from app.application.use_cases.list_vehicle_by_status_use_case import ListVehiclesByStatusUseCase
from app.domain.models.vehicle_status import VehicleStatusEnum
from app.infra.api.schemas.vehicle_dto import VehicleCreateRequest, VehicleResponse, VehicleUpdateRequest
from app.application.use_cases.create_vehicle import CreateVehicleUseCase
from app.infra.database.database import get_session
from app.infra.persistence.repositories.vehicle_repository_impl import VehicleRepositoryImpl

router = APIRouter(prefix="/vehicle", tags=["Vehicle"])

def get_vehicle_repository(session: AsyncSession = Depends(get_session)):
    return VehicleRepositoryImpl(session)

def get_create_vehicle_use_case(repo: VehicleRepositoryImpl = Depends(get_vehicle_repository)):
    return CreateVehicleUseCase(vehicle_repository=repo)

def get_update_vehicle_use_case(
    repo: VehicleRepositoryImpl = Depends(get_vehicle_repository),
):
    return UpdateVehicleUseCase(vehicle_repository=repo)

def get_list_by_status_use_case(session: AsyncSession = Depends(get_session)):
    repo = VehicleRepositoryImpl(session)
    return ListVehiclesByStatusUseCase(repo)


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

@router.patch("/{vehicle_id}", response_model=VehicleResponse)
async def update_vehicle(
    vehicle_id: int,
    payload: VehicleUpdateRequest,
    use_case: UpdateVehicleUseCase = Depends(get_update_vehicle_use_case)
):
    vehicle = await use_case.execute(
        vehicle_id=vehicle_id,
        data=payload.model_dump(exclude_unset=True)
    )
    return vehicle


@router.get("/list")
async def list_vehicles(
    status: VehicleStatusEnum,
    use_case: ListVehiclesByStatusUseCase = Depends(get_list_by_status_use_case)
):
    return await use_case.execute(status)
     