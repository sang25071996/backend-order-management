from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.repositories.product_repository import ProductRepository
from app.responses.product_response import ProductResponse
from app.schemas.product import ProductCreate
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/")
async def create_product(product: ProductCreate, session: AsyncSession = Depends(get_session)) -> ProductResponse:
    product_repository = ProductRepository(session)
    product_service = ProductService(product_repository)
    return product_service.create_product(product)


@router.get("/{product_id}")
async def get_product_by_id(product_id: int, session: AsyncSession = Depends(get_session)) -> ProductResponse:
    product_repository = ProductRepository(session)
    product_service = ProductService(product_repository)
    product = await product_service.get_by_id(product_id)
    if product is None:
        return {"error": "Product not found"}
    return product