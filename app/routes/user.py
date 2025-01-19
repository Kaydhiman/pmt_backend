from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user import create_user, get_all_users, get_user_by_email
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

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_new_user(user: UserCreate, db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1]))):
    try:
        if current_user:
            if get_user_by_email(db, user.email):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
            return create_user(db, user)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")

@router.get("/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1]))):
    try:
        if current_user:
            return get_all_users(db)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")
