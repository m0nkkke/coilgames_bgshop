from fastapi import APIRouter

from schemas.user import UserRead, UserUpdate
from core.auth.fastapi_users import fastapi_users
from core.config import settings
from api.dependencies.auth.backend import auth_backend

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=['USERS'],
)

# /me 
# /{id}
router.include_router(
    router = fastapi_users.get_users_router(UserRead, UserUpdate),
)