from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.task_type import TaskTypeCreate, TaskTypeResponse
from app.services.task_type import create_task_type, get_all_task_types
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

@router.post("/", response_model=TaskTypeResponse, status_code=status.HTTP_201_CREATED)
def create_new_task_type(task_type: TaskTypeCreate, db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1]))):
    try:
        if current_user:
            return create_task_type(db, task_type)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")

@router.get("/", response_model=List[TaskTypeResponse])
def list_task_types(db: Session = Depends(get_db)):
    return get_all_task_types(db)
