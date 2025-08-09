from fastapi import APIRouter, HTTPException

from app.dao.data import data_users
router = APIRouter(prefix='/api/users', tags=['/api/users'])

@router.get("/all", summary="LIST of all users")
async def get_all():
    return data_users


@router.get("/{user_id}", summary="Find users by id")
async def get_id(user_id: int):
    result = next((item for item in data_users if item["id"] == user_id), None)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Запись с id={user_id} не найдена")
    return result
