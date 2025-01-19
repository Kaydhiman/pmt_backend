from pydantic import BaseModel, Field
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: int
    task_type_id: int
    task_status_id: int
    created_by: int

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, example="Updated Task Title")
    description: Optional[str] = Field(None, example="Updated description of the task")
    task_status_id: Optional[int] = Field(None, example=2)
    assigned_to: Optional[int] = Field(None, example=3)

    class Config:
        from_attributes = True