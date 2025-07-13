from app.core.config import async_session

async def get_session():
    async with async_session() as session:
        yield session

