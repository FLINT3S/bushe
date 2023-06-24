import os

import uvicorn
from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware

from data.model.order import Order
from data.model.orderstatus import OrderStatus
from data.model.deliverytask import DeliveryTask
from data.model.deliverytaskstatus import DeliveryTaskStatus
from data.model.user import User

from data.databaseservice import DatabaseService
from services.service import APIService

database_service = DatabaseService(
    f"postgresql+asyncpg://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@185.154.193.39:5432/{os.environ['POSTGRES_DB']}")
api = APIService(database_service)


@api.app.on_event("startup")
async def init_db():
    async with database_service.engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


api.app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.app.get("/status")
async def root():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:api.app", port=3000, reload=True, workers=1)
    api.database.init_meta_data()
