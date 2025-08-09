from fastapi import APIRouter, HTTPException
from app.api.unknown.schemas import CreateUnknown
from app.dao.data import data_unknown

data_unknown = data_unknown()
router = APIRouter(prefix='/api/unknown', tags=['/api/unknown'])


@router.get("/all", summary="LIST of all unknown")
async def get_all():
    return data_unknown


@router.get("/{unknown_id}", summary="Find unknown by id")
async def get_id(unknown_id: int):
    result = next((item for item in data_unknown if item["id"] == unknown_id), None)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Запись с id={unknown_id} не найдена")
    return result
