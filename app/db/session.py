from app.db.config import *
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

DATABASE_URL = f"{DB_CONNECTION}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

async_engine = create_async_engine(
    url=DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10
)

SessionLocal = async_sessionmaker(
    bind=async_engine, autoflush=False, autocommit=False)


async def get_async_session():
    async_session = SessionLocal()
    yield async_session
