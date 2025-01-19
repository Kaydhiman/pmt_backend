from sqlalchemy.orm import Session
from app.models.task_status import TaskStatus
from app.schemas.task_status import TaskStatusCreate

def create_task_status(db: Session, task_status: TaskStatusCreate):
    db_task_status = TaskStatus(name=task_status.name, description=task_status.description)
    db.add(db_task_status)
    db.commit()
    db.refresh(db_task_status)
    return db_task_status

def get_all_task_statuses(db: Session):
    return db.query(TaskStatus).all()
