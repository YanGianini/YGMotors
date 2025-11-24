from pydantic import BaseModel

class SaleCreateRequest(BaseModel):
    buyer_cpf: str


class SaleResponse(BaseModel):
    id: int
    vehicle_id: int
    buyer_cpf: str

    class Config:
        from_attributes = True

