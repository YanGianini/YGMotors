from abc import ABC, abstractmethod
from app.domain.models.sale import Sale


class SaleRepository(ABC):

    @abstractmethod
    async def create(self, sale: Sale) -> Sale:
        pass
