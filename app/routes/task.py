from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task import create_task, delete_task, get_all_tasks, get_task_by_id, update_task
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

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1, 2, 3]))):
    try:
        if current_user:
            return create_task(db, task)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")

@router.get("/", response_model=List[TaskResponse])
def list_tasks(db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1, 2, 3]))):
    try:
        if current_user:
            return get_all_tasks(db)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1, 2, 3]))):
    try:
        if current_user:
            task = get_task_by_id(db, task_id)
            if not task:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
            return task
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")

@router.put("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_new_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1, 2, 3]))):
    try:
        if current_user:
            return update_task(db=db, task_id=task_id, task_update=task, current_user=current_user)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_by_id(task_id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1, 2, 3]))):
    try:
        if current_user:
            if not delete_task(db, task_id):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")
