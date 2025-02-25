from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse

from app.db.core import get_all_users
from app.db.service import get_validated_users
from app.users.models import PublicUser

users_router = APIRouter()

@users_router.get("/")
async def get_users():
    return JSONResponse({"users": [user.model_dump() for user in await get_validated_users()]})
