from pydantic import BaseModel

class TaskTypeBase(BaseModel):
    name: str
    description: str

class TaskTypeCreate(TaskTypeBase):
    pass

class TaskTypeResponse(TaskTypeBase):
    id: int

    class Config:
        from_attributes = True
