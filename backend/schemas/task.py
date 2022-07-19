from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from core.py_object_id import PyObjectId


class TaskBase(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class TaskCreate(TaskBase):
    title: str = Field(...)
    description: str = Field(...)
    completed: bool = False


class TaskUpdate(TaskBase):
    pass


class TaskInDBBase(TaskBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    description: str
    completed: bool


class Task(TaskInDBBase):
    pass


class TaskInDB(TaskInDBBase):
    pass
