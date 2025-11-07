from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from core.auth.transport import cookie_transport
from .strategy import get_database_strategy

auth_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=cookie_transport,
    get_strategy=get_database_strategy,
)