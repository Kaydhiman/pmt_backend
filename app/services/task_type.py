from sqlalchemy.orm import Session
from app.models.task_type import TaskType
from app.schemas.task_type import TaskTypeCreate

def create_task_type(db: Session, task_type: TaskTypeCreate):
    db_task_type = TaskType(name=task_type.name, description=task_type.description)
    db.add(db_task_type)
    db.commit()
    db.refresh(db_task_type)
    return db_task_type

def get_all_task_types(db: Session):
    return db.query(TaskType).all()
