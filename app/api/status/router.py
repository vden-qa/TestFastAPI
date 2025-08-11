from fastapi import APIRouter, HTTPException
from http import HTTPStatus

from app.api.status.schemas import AppStatus
from app.api.users.schemas import User
from app.dao.data import data_users

data_users = data_users()

router = APIRouter(prefix='/api/status', tags=['/api/status'])

@router.get("",
            summary="Check status",
            status_code=HTTPStatus.OK)
async def status()  -> AppStatus:
    return AppStatus(users=bool(data_users))


