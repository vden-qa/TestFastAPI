from fastapi import APIRouter, HTTPException, Depends
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.users.dao import get_all_users, get_user_by_id, create_user, update_user, delete_user
from app.api.users.schemas import User, UserCreate, UserUpdate
from app.database import get_async_session

router = APIRouter(prefix='/api/users', tags=['/api/users'])


@router.get("", summary="LIST of all users", status_code=HTTPStatus.OK, response_model=list[User])
async def get_all(session: AsyncSession = Depends(get_async_session)) -> list[User]:
    users_ = await get_all_users(session)
    return users_


@router.get("/{user_id}", summary="Find users by id", status_code=HTTPStatus.OK, response_model=User)
async def get_id(user_id: int, session: AsyncSession = Depends(get_async_session)) -> User:
    user_ = await get_user_by_id(session, user_id)
    if user_ is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return user_


@router.post("", summary="Create user", status_code=HTTPStatus.CREATED, response_model=User)
async def create_user_endpoint(user_data: UserCreate, session: AsyncSession = Depends(get_async_session)) -> User:
    user_ = await create_user(session, user_data)
    return user_


@router.put("/{user_id}", summary="Update user", status_code=HTTPStatus.OK, response_model=User)
async def update_user_endpoint(user_id: int, user_data: UserUpdate,
                               session: AsyncSession = Depends(get_async_session)) -> User:
    user_ = await update_user(session, user_id, user_data)
    if user_ is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return user_


@router.delete("/{user_id}", summary="Delete user", status_code=HTTPStatus.NO_CONTENT)
async def delete_user_endpoint(user_id: int, session: AsyncSession = Depends(get_async_session)):
    success = await delete_user(session, user_id)
    if not success:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return None
