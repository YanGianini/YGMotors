from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.application.ports.vehicle_repository import VehicleRepository
from app.domain.models.vehicle import Vehicle
from app.infra.database.tables import vehicle_table


class VehicleRepositoryImpl(VehicleRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, vehicle: Vehicle) -> Vehicle:
        query = (
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

        result = await self.session.execute(query)
        new_id = result.scalar()
        await self.session.commit()

        vehicle.id = new_id
        return vehicle


    async def get_by_id(self, vehicle_id: int) -> Vehicle | None:
        query = select(vehicle_table).where(vehicle_table.c.id == vehicle_id)
        result = await self.session.execute(query)
        row = result.fetchone()
        if not row:
            return None

        return Vehicle(**row._mapping)


    async def update(self, vehicle_id: int, data: dict) -> Vehicle:
        query = (
            update(vehicle_table)
            .where(vehicle_table.c.id == vehicle_id)
            .values(**data)
            .returning(vehicle_table)
        )

        result = await self.session.execute(query)
        await self.session.commit()

        row = result.fetchone()
        if not row:
            return None

        return Vehicle(**row._mapping)
    
    async def list_by_status(self, status: str) -> list[Vehicle]:
        query = (
            select(vehicle_table)
            .where(vehicle_table.c.status == status)
            .order_by(vehicle_table.c.price.asc())
        )
        result = await self.session.execute(query)
        rows = result.fetchall()

        if not rows:
            return []
        
        return [Vehicle(**row._mapping) for row in rows]
    
    