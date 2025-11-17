from app.application.ports.vehicle_repository import VehicleRepository
from app.domain.models.vehicle import Vehicle


class ListVehiclesByStatusUseCase:
    def __init__(self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    async def execute(self, status: str) -> list[Vehicle]:
        return await self.vehicle_repository.list_by_status(status)
    
