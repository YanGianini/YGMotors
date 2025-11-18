from datetime import datetime
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.application.ports.vehicle_repository import VehicleRepository
from app.domain.models.vehicle import Vehicle
from app.infra.database.models.vehicle_orm import VehicleORM
from app.infra.database.tables import vehicle_table


class VehicleRepositoryImpl(VehicleRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, vehicle: Vehicle) -> Vehicle:
        orm_obj = VehicleORM(
            brand=vehicle.brand,
            model=vehicle.model,
            year=vehicle.year,
            color=vehicle.color,
            price=vehicle.price,
            status=vehicle.status,
            created_at=vehicle.created_at,
            updated_at=vehicle.updated_at
        )

        self.session.add(orm_obj)
        await self.session.commit()
        await self.session.refresh(orm_obj)

        return Vehicle.from_orm(orm_obj)


    async def get_by_id(self, vehicle_id: int) -> Vehicle | None:
        orm_obj = await self.session.get(VehicleORM, vehicle_id)
        if not orm_obj:
            return None
        return Vehicle.from_orm(orm_obj)


    async def update(self, vehicle_id: int, data: dict) -> Vehicle:
        orm_obj = await self.session.get(VehicleORM, vehicle_id)
        if not orm_obj:
            return None

        for field, value in data.items():
            if hasattr(orm_obj, field):
                setattr(orm_obj, field, value)

        orm_obj.updated_at = datetime.utcnow()

        self.session.add(orm_obj)
        await self.session.commit()
        await self.session.refresh(orm_obj)

        return Vehicle.from_orm(orm_obj)
    
    async def list_by_status(self, status: str) -> list[Vehicle]:
        query = (
            select(VehicleORM)
            .where(VehicleORM.status == status)
            .order_by(VehicleORM.price.asc())
        )

        result = await self.session.execute(query)
        rows = result.scalars().all()

        return [Vehicle.from_orm(r) for r in rows]
    
    