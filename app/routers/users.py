from typing import Optional, Union
from mongoengine.errors import NotUniqueError
from app.schemas import users as users_schemas
from app.models import users as model_users
from fastapi import APIRouter, HTTPException
from app.database import client

client = client


router = APIRouter(
    tags=['Users'],
    prefix='/user',
)


@router.post('/', response_model=users_schemas.UserOut)
async def create(request: users_schemas.User):
    new_user = model_users.User(**request.dict())
    try:
        new_user.save()
    except NotUniqueError:
        raise HTTPException(status_code=400, detail='Email exists yet')
    new_user = new_user.reload()

    return new_user.object()
