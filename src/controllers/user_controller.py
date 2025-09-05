from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.services.user_service import create_user, get_user_by_email
from src.schemas.user import UserCreate, UserResponse

def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user_in)
