from pydantic import Field

from backend.db.database import Base


class Task(Base):
    id: str = Field(...)
    name: str = Field(...)
    completed: bool = False
