import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.api.api_v1.api import api_router
from backend.core.config import settings
from backend.db.database import client, database

app = FastAPI()


@app.on_event("startup")
async def start_db_client():
    app.db_client = client
    app.db_database = database


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(CORSMiddleware, allow_origins=settings.BACKEND_CORS_ORIGINS, allow_credentials=True,
                       allow_methods=["*"], allow_headers=["*"])


@app.on_event("shutdown")
async def shutdown_db_client():
    app.db_client.close()


app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, reload=settings.DEBUG_MODE, port=settings.PORT)
