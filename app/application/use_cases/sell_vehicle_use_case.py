from datetime import datetime
from app.domain.models.sale import Sale
from app.domain.models.vehicle_status import VehicleStatusEnum


class SellVehicleUseCase:

    def __init__(self, vehicle_repository, sale_repository):
        self.vehicle_repository = vehicle_repository
        self.sale_repository = sale_repository

    async def execute(self, vehicle_id: int, buyer_cpf: str) -> Sale:
        vehicle = await self.vehicle_repository.get_by_id(vehicle_id)
        if not vehicle:
            raise ValueError("Vehicle not found")
        
        if vehicle.status != VehicleStatusEnum.AVAILABLE:
            raise ValueError("Vehicle not available for sale")

        sale = Sale(
            id=None,
            vehicle_id=vehicle_id,
            buyer_cpf=buyer_cpf,
            sale_date=datetime.utcnow(),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        sale = await self.sale_repository.create(sale)

        await self.vehicle_repository.update(vehicle_id, {"status": VehicleStatusEnum.SOLD})

        return sale
