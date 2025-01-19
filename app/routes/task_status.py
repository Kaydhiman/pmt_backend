from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task_status import TaskStatusCreate, TaskStatusResponse
from app.services.task_status import create_task_status, get_all_task_statuses
from app.config import SessionLocal
from typing import List
from app.schemas.auth import TokenData
from app.services.auth import authorize_user

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TaskStatusResponse, status_code=status.HTTP_201_CREATED)
def create_new_task_status(task_status: TaskStatusCreate, db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1]))):
    try:
        if current_user:
            return create_task_status(db, task_status)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")

@router.get("/", response_model=List[TaskStatusResponse])
def list_task_statuses(db: Session = Depends(get_db)):
    return get_all_task_statuses(db)
