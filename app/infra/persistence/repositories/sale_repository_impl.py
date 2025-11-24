from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from app.application.ports.sale_repository import SaleRepository
from app.domain.models.sale import Sale
from app.infra.database.models.sale_orm import SaleORM

class SaleRepositoryImpl(SaleRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, sale: Sale) -> Sale:
        stmt = (
            insert(SaleORM)
            .values(
                vehicle_id=sale.vehicle_id,
                buyer_cpf=sale.buyer_cpf,
                sale_date=sale.sale_date,
                created_at=sale.created_at,
                updated_at=sale.updated_at
            )
            .returning(SaleORM.id)
        )

        result = await self.session.execute(stmt)
        new_id = result.scalar()
        await self.session.commit()

        sale.id = new_id
        return sale
