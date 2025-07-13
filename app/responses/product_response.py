from app.models.Product import Product
from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float

    @classmethod
    def from_orm(cls, product: Product):
        return cls(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
        )
