import datetime

from fastapi.types import BaseModel


class PublicUser(BaseModel):
    user_id: int
    user_email: str
    user_name: str | None
