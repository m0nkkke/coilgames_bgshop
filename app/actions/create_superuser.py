import asyncio
import contextlib
from datetime import date, datetime
from os import getenv

from models.user import User
from core.auth.user_manager import UserManager
from db import db_helper
from schemas.user import UserCreate
from api.dependencies.auth.user_manager import get_user_manager
from api.dependencies.auth.users import get_users_db

get_user_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

default_email = getenv("DEFAULT_EMAIL", "admin@admin.com")
default_password = getenv("DEFAULT_PASSWORD", "admin")
default_is_active = True
default_is_superuser = True
default_is_verified = True
display_name = getenv("ADMIN_NAME", "admin")
birthday_date = datetime.strptime("2025-11-06", "%Y-%m-%d").date()
gender= 'М'

async def create_user(
        user_manager: UserManager,
        user_create: UserCreate,
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
        email: str = default_email,
        password: str = default_password,
        is_active: bool = default_is_active,
        is_superuser: bool = default_is_superuser,
        is_verified: bool = default_is_verified,
        display_name: str = display_name,
        birthday_date: date = birthday_date,

        gender: str = gender,
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
        display_name= display_name,
        birthday_date= birthday_date,
        gender=gender,
    )
    async with db_helper.session_factory() as session:
        async with get_user_db_context(session) as users_db:
            async with get_user_manager_context(users_db) as user_manager:
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create,
                )

if __name__ == "__main__":
    asyncio.run(create_superuser())