from app.application.ports.vehicle_repository import VehicleRepository
from app.domain.models.vehicle import Vehicle


class CreateVehicleUseCase:
    def __init__(self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    async def execute(self, brand: str, model: str, year: int, color: str, price: float) -> Vehicle:
        if price <= 0:
            raise ValueError("Preço deve ser maior que zero.")
        vehicle = Vehicle.create(
            brand=brand,
            model=model,
            year=year,
            color=color,
            price=price
        )

        return await self.vehicle_repository.create(vehicle)
