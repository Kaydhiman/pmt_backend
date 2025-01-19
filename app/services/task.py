from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.models.user import User

def create_task(db: Session, task: TaskCreate):
    db_task = Task(
        title=task.title,
        description=task.description,
        assigned_to=task.assigned_to,
        task_type_id=task.task_type_id,
        task_status_id=task.task_status_id,
        created_by=task.created_by
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(
    db: Session, task_id: int, task_update: TaskUpdate, current_user: User
):
    task = get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )

    # Check permissions
    if current_user.role.name != "Admin" and task.assigned_to != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to update this task.",
        )

    # Update the task fields
    for key, value in task_update.dict(exclude_unset=True).items():
        setattr(task, key, value)

    # Commit the changes to the database
    db.commit()
    db.refresh(task)

    return task

def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)
    if task:
        db.delete(task)
        db.commit()
        return True
    return False
