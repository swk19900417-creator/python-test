from fastapi import FastAPI
from app.interface.api.v1.auth_router import auth_router
from app.interface.api.v1.order_router import order_router
from config.settings import settings
from tortoise import Tortoise
import uvicorn
from contextlib import asynccontextmanager


async def init_db():
    await Tortoise.init(db_url=settings.get_db_url, modules={"models": ["app.infrastructure.database.orm_models"]})
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()


def create_app() -> FastAPI:
    """创建FastAPI应用"""
    app = FastAPI(title=settings.app_name, description="用户服务接口", version=settings.app_version, lifespan=lifespan)
    app.include_router(auth_router, prefix="/api/v1", tags=["认证"])
    app.include_router(order_router, prefix="/api/v1", tags=["订单"])
    return app


app = create_app()


@app.get("/")
async def root():
    return {"message": "Welcome To DDD Application"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=settings.debug)
