from datetime import date, datetime
from typing import Dict, Optional
from models.types import UserIdType

from fastapi_users import schemas

from .enums.genders import GenderEnum


class UserRead(schemas.BaseUser[UserIdType]): 
    display_name: str
    birthday_date: date
    gender: GenderEnum
    is_email_newsletter: bool
    level: int
    level_experience: int
    image: Optional[str]
    meta_data: Dict
    created_at: datetime
    updated_at: datetime


class UserCreate(schemas.BaseUserCreate):
    display_name: str
    birthday_date: date 
    gender: GenderEnum
    is_email_newsletter: Optional[bool] = False
    image: Optional[str] = None
    # level: int = 0
    # level_experience: int = 0
    meta_data: Dict = {}

class UserUpdate(schemas.BaseUserUpdate):
    display_name: Optional[str]
    birthday_date: Optional[date]
    gender: Optional[str]
    image: Optional[str]
    is_email_newsletter: Optional[bool]
    meta_data: Optional[Dict]