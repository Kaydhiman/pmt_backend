from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.role import RoleCreate, RoleResponse
from app.services.role import (create_role, delete_role, get_all_roles, get_role_by_id,
    update_role_by_id)
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

@router.post("/", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create_new_role(role: RoleCreate, db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1]))):
    try:
        if current_user:
            return create_role(db, role)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")

@router.get("/", response_model=List[RoleResponse])
def list_roles(db: Session = Depends(get_db)):
    return get_all_roles(db)

@router.get("/{role_id}", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def get_role(role: RoleCreate, db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1]))):
    try:
        if current_user:
            return get_role_by_id(db, role)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")    
    
@router.put("/{role_id}", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def update_role(role: RoleCreate, db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1]))):
    try:
        if current_user:
            return update_role_by_id(db, role, role)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")
    
@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role_by_id(role_id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(authorize_user([1]))):
    try:
        if current_user:
            if not delete_role(db, role_id):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access to this resource")
