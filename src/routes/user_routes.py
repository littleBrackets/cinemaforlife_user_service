from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.services.auth_service import authenticate_user, login_user

router = APIRouter()

def login(email: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = login_user(user.email)
    return {"access_token": token, "token_type": "bearer"}
