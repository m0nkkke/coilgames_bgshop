from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    String,
    Boolean,
    Integer,
    Date,
    TIMESTAMP,
    text,
    JSON,
)
from datetime import datetime, date

from db.base import Base
from .mixins.id_int_pk import IdIntPkMixin
from .types import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):
    display_name: Mapped[str] = mapped_column(String(200), nullable=False)
    birthday_date: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[str] = mapped_column(String(25), nullable=False)
    is_email_newsletter: Mapped[bool] = mapped_column(Boolean, default=False)
    level: Mapped[int] = mapped_column(Integer, default=0, server_default=text("0"),)
    level_experience: Mapped[int] = mapped_column(Integer, default=0, server_default=text("0"),)
    image: Mapped[str | None] = mapped_column(String(1000))
    role: Mapped[str] = mapped_column(String(50), server_default=text("'user'"))
    meta_data: Mapped[dict] = mapped_column(JSON, server_default=text("'{}'::jsonb"))
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=text("now()")
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=text("now()")
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)