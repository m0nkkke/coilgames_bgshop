from fastapi_users import FastAPIUsers

from models.user import User
from models.types import UserIdType

from api.dependencies.auth.user_manager import get_user_manager
from api.dependencies.auth.backend import auth_backend

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(active=True)
current_super_user = fastapi_users.current_user(active=True, superuser=True)