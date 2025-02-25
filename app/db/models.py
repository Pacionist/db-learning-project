from sqlalchemy import DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, Mapped


class TimestampMixin:
    created_at = mapped_column(DateTime, server_default=text("TIMEZONE('utc', now())"))
    updated_at = mapped_column(DateTime, server_default=text("TIMEZONE('utc', now())"),
                        onupdate=text("TIMEZONE('utc', now())"))

Base = declarative_base(cls=TimestampMixin)

class User(Base):
    __tablename__  = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement="auto")
    email: Mapped[str]
    username: Mapped[str | None]
    password: Mapped[str]
    is_admin: Mapped[bool]
