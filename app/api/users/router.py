from fastapi import APIRouter, HTTPException
from http import HTTPStatus

from app.api.users.schemas import User
from app.dao.data import data_users

data_users = data_users()
for user in data_users:
    User.model_validate(user)
router = APIRouter(prefix='/api/users', tags=['/api/users'])

@router.get("",
            summary="LIST of all users",
            status_code=HTTPStatus.OK)
async def get_all() -> list[User]:
    return data_users


@router.get("/{user_id}",
            summary="Find users by id",
            status_code=HTTPStatus.OK)
async def get_id(user_id: int) -> User:
    result = next((item for item in data_users if item["id"] == user_id), None)
    if result is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return result
