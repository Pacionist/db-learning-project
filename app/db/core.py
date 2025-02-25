import asyncio

from sqlalchemy import text, select

from app.db.models import Base, User
from app.db.session import async_engine, get_async_session


async def get_all_users():
    session = await anext(get_async_session())
    query = select(User.id, User.username, User.email)
    result = await session.execute(query)
    await session.close()
    users = result.all()
    return users

async def add_test_user():
    new_test_user = User(email="sogrdg@dgaedf.er", username="Ptica", password="11121", is_admin=False)
    session = await anext(get_async_session())
    session.add(new_test_user)
    await session.commit()

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
