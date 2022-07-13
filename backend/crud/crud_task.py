from fastapi import Request

from backend.crud.crud_base import CRUDBase
from backend.models.task_model import Task
from backend.schemas.task import TaskCreate, TaskUpdate


class CRUDTask(CRUDBase[Task, TaskCreate, TaskUpdate]):
    async def delete_all(self, request: Request):
        return await request.app.db_database[self.collection].delete_many({})


crud_task = CRUDTask('tasks')
