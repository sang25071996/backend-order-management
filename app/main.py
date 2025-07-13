from fastapi import FastAPI
from app.routers import products_router

app = FastAPI()

app.include_router(products_router, tags=["products"])


