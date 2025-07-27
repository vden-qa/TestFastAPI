from fastapi import APIRouter, HTTPException
from app.api.unknown.schemas import CreateUnknown
from app.dao.data import data_unknown

data_unknown = data_unknown()
router = APIRouter(prefix='/api/unknown', tags=['/api/unknown'])


@router.get("/all", summary="LIST of all unknown")
async def get_all():
    return data_unknown


@router.get("/{id}", summary="Find unknown by id")
async def get_id(id: int):
    result = next((item for item in data_unknown if item["id"] == id), None)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Запись с id={id} не найдена")
    return result


@router.post("/create", summary="Create Unknown")
async def create_unknown(
        add_data: CreateUnknown
):
    found_item = next((item for item in data_unknown if item["id"] == add_data.id), None)
    if found_item:
        raise HTTPException(status_code=404, detail=f"Запись с id={add_data.id} уже существует")
    else:
        data_unknown.append(add_data.dict())
    return add_data


@router.delete("/delete/{id}", summary="Delete Unknown by id")
async def delete_unknown(id: int):
    # result = next((item for item in data_unknown if item["id"] == id), None)
    # if result is None:
    #     raise HTTPException(status_code=404, detail=f"Запись с id={id} не найдена")
    return data_unknown
