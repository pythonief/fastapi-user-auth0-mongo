from typing import List

from app.utils import *
from bson.objectid import ObjectId
from pydantic import BaseModel
from pydantic.networks import EmailStr


class User(BaseModel):
    fullname: str
    email: EmailStr
    scopes: List[str] = []


class UserOut(BaseModel, MongoMixinBaseModel):
    fullname: str
    email: EmailStr
