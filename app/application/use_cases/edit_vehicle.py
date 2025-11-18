from typing import Dict, Any
from typing import Any
from app.application.ports.vehicle_repository import VehicleRepository
from app.domain.models.vehicle import Vehicle


class UpdateVehicleUseCase:
    def __init__(self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    async def execute(self, vehicle_id: int, data: Dict[str, Any]) -> Vehicle:
        vehicle = await self.vehicle_repository.update(vehicle_id, data)
        if not vehicle:
            raise ValueError("Vehicle not found")
        return vehicle

