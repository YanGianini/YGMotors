from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.application.ports.vehicle_repository import VehicleRepository
from app.domain.models.vehicle import Vehicle
from app.infra.database.tables import vehicle_table


class VehicleRepositoryImpl(VehicleRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, vehicle: Vehicle) -> Vehicle:
        stmt = (
            insert(vehicle_table)
            .values(
                brand=vehicle.brand,
                model=vehicle.model,
                year=vehicle.year,
                color=vehicle.color,
                price=vehicle.price,
                status=vehicle.status.value,
                created_at=vehicle.created_at,
                updated_at=vehicle.updated_at
            )
            .returning(vehicle_table.c.id)
        )

        result = await self.session.execute(stmt)
        new_id = result.scalar()
        await self.session.commit()

        vehicle.id = new_id
        return vehicle

    async def get_by_id(self, vehicle_id: int):
        raise NotImplementedError
