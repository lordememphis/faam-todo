from fastapi import APIRouter

from backend.api.api_v1.endpoints import tasks

api_router = APIRouter()
api_router.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
