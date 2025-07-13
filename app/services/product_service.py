from app.converter.ProductConverter import ProductConverter
from app.repositories.product_repository import ProductRepository
from app.responses.product_response import ProductResponse
from app.schemas.product import ProductCreate


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def create_product(self, product_create: ProductCreate) -> ProductResponse:
        product = await self.product_repository.create_product(product_create)
        return ProductConverter.convert(product)

    async def get_by_id(self, product_id: int) -> ProductResponse | None:
        product = await self.product_repository.get_by_id(product_id)
        if product is None:
            return None
        return ProductConverter.convert(product)