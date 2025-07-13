from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.models.Product import Product
from app.schemas.product import ProductCreate


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_product(self, product_create: ProductCreate) -> Product:
        product = Product(name=product_create.name,
                          description=product_create.description,
                          price=product_create.price)
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product

    async def get_by_id(self, product_id: int) -> Product | None:
        result = await self.session.execute(
            text("SELECT * FROM product WHERE id = :id"), {"id": product_id}
        )
        product = result.fetchone()
        if product is None:
            return None
        return Product(**product._asdict())