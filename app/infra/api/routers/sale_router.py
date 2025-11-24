from fastapi import APIRouter, Depends
from app.application.use_cases.sell_vehicle_use_case import SellVehicleUseCase
from app.infra.database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

from app.infra.api.schemas.sale_dto import SaleCreateRequest, SaleResponse
from app.infra.persistence.repositories.vehicle_repository_impl import VehicleRepositoryImpl
from app.infra.persistence.repositories.sale_repository_impl import SaleRepositoryImpl

router = APIRouter(prefix="/vehicle", tags=["Sale"])

def get_sell_vehicle_use_case(session: AsyncSession = Depends(get_session)):
    vehicle_repo = VehicleRepositoryImpl(session)
    sale_repo = SaleRepositoryImpl(session)
    return SellVehicleUseCase(vehicle_repo, sale_repo)

@router.post("/{vehicle_id}/sell", response_model=SaleResponse)
async def sell_vehicle(
    vehicle_id: int,
    payload: SaleCreateRequest,
    use_case: SellVehicleUseCase = Depends(get_sell_vehicle_use_case),
):
    sale = await use_case.execute(vehicle_id, payload.buyer_cpf)
    return sale

