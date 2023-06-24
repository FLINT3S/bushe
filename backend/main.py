import os

from starlette.middleware.cors import CORSMiddleware

import uvicorn

from backend.data.databaseservice import DatabaseService
from backend.services.service import APIService

api = APIService(DatabaseService("postgresql+asyncpg://" + os.environ['POSTGRES_USER'] + ":"
                                 + os.environ['POSTGRES_PASSWORD'] + "@185.154.193.39:5432/" + os.environ["POSTGRES_DB"]))

api.app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run("main:api.app", port=3000, reload=True, workers=1)
    api.database.init_meta_data()
