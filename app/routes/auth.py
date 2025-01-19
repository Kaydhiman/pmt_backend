from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import Token
from app.services.auth import authenticate_user, create_access_token
from app.config import SessionLocal
from datetime import timedelta

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login", response_model=Token)
def login_for_access_token(email: str, password: str, db: Session = Depends(get_db)):
    """Authenticate user and return a JWT access token."""
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.id, "role": user.role_id}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
