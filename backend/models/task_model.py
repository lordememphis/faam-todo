from pydantic import Field

from backend.db.database import Base


class Task(Base):
    id: str = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    completed: bool = False
