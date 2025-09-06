from contextlib import asynccontextmanager
from app.database import init_db
import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from app.api.users.router import router as router_users
from app.api.status.router import router as router_status


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title="TestFastAPI",
    description="Тестовый проект на FastAPI",
    version="1.0.0",
    lifespan=lifespan
)

add_pagination(app)


@app.get("/")
async def home_page():
    return {
        "message": "Добро пожаловать! TestFastAPI"
    }


app.include_router(router_users)
app.include_router(router_status)
