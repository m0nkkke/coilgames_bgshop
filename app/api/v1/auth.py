from fastapi import APIRouter

from schemas.user import UserRead, UserCreate
from core.auth.fastapi_users import fastapi_users
from core.config import settings
from api.dependencies.auth.backend import auth_backend

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=['AUTH'],
)

# /login
# /logout
router.include_router(
    router=fastapi_users.get_auth_router(auth_backend),
)

# /register
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

# /request-verify-token
# /verify
router.include_router(
    router = fastapi_users.get_verify_router(UserRead),
)

# /forgot-password
# /reset-password
router.include_router(
    router=fastapi_users.get_reset_password_router(),
)