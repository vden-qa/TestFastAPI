from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, Iterable

from app.api.users.models import User as UserModel
from app.api.users.schemas import UserCreate, UserUpdate


async def get_all_users(session: AsyncSession) -> Iterable[UserModel]:
    result = await session.execute(select(UserModel))
    return result.scalars().all()


async def get_user_by_id(session: AsyncSession, user_id: int) -> Optional[UserModel]:
    result = await session.execute(select(UserModel).where(UserModel.id == user_id))
    return result.scalar_one_or_none()


async def create_user(session: AsyncSession, user_data: UserCreate) -> UserModel:
    db_user = UserModel()
    db_user.email = str(user_data.email)
    db_user.first_name = user_data.first_name
    db_user.last_name = user_data.last_name
    db_user.avatar = str(user_data.avatar)

    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user


async def update_user(session: AsyncSession, user_id: int, user_data: UserUpdate) -> Optional[UserModel]:
    result = await session.execute(select(UserModel).where(UserModel.id == user_id))
    user_ = result.scalar_one_or_none()

    if user_ is None:
        return None

    update_data_ = user_data.model_dump(exclude_unset=True)
    if "avatar" in update_data_:
        update_data_["avatar"] = str(update_data_["avatar"])

    for field, value in update_data_.items():
        setattr(user_, field, value)

    await session.commit()
    await session.refresh(user_)
    return user_


async def delete_user(session: AsyncSession, user_id: int) -> bool:
    user = await get_user_by_id(session, user_id)
    if user is None:
        return False
    await session.delete(user)
    await session.commit()
    return True
