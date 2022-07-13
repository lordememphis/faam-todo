from typing import List

from fastapi import APIRouter, Request, Body, HTTPException, status

from backend.crud.crud_task import crud_task
from backend.schemas.task import Task, TaskCreate, TaskUpdate

router = APIRouter()


@router.post("", response_model=Task)
async def create_task(request: Request, task: TaskCreate = Body(...)):
    return await crud_task.create(request, task)


@router.get("", response_model=List[Task])
async def get_tasks(request: Request, page: int = 0, size: int = 10):
    return await crud_task.get_multi(request, page, size)


@router.get("/{task_id}", response_model=Task)
async def get_task(request: Request, task_id: str):
    task = await crud_task.get_by_id(request, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task '{task_id}' was not found")
    return task


@router.put("/{task_id}", response_model=Task)
async def update_task(request: Request, task_id: str, task: TaskUpdate):
    update = await crud_task.update(request, task_id, task)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task '{task_id}' was not found")
    return update


@router.delete("/{task_id}", response_model=str)
async def delete_task(request: Request, task_id: str):
    if not await crud_task.delete(request, task_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task '{task_id}' was not found")
    return "Task deleted"


@router.delete("", response_model=str, include_in_schema=False)
async def delete_all_tasks(request: Request):
    if not await crud_task.delete_all(request):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tasks could not be deleted")
    return "All tasks deleted"
