from fastapi import APIRouter, Depends
from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.status.dao import check_availability
from app.api.status.schemas import AppStatus
from app.database import get_async_session

router = APIRouter(prefix='/api/status', tags=['/api/status'])

@router.get("",
            summary="Check status",
            status_code=HTTPStatus.OK)
async def status(session: AsyncSession = Depends(get_async_session)) -> AppStatus:
    status_ = await check_availability(session)
    return AppStatus(database=status_)
