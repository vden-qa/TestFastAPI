from fastapi import FastAPI
from app.api.users.router import router as router_users
from app.api.unknown.router import router as router_unknown
app = FastAPI()

@app.get("/")
async def home_page():
    return {
        "message": "Добро пожаловать! TestFastAPI"
    }

app.include_router(router_users)
app.include_router(router_unknown)