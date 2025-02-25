import asyncio

from app.db.core import get_all_users
from app.users.models import PublicUser


async def get_validated_users():
    db_users = await get_all_users()
    users = []
    for db_user in db_users:
        user = PublicUser(user_id=db_user[0], user_name=db_user[1], user_email=db_user[2])
        users.append(user)
    return users
