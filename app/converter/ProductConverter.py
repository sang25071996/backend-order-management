from app.models.Product import Product
from app.responses.product_response import ProductResponse


class ProductConverter:
    @staticmethod
    def convert(product: Product) -> ProductResponse:
        return ProductResponse.from_orm(product)
