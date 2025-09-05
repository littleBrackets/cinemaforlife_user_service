from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.controllers.auth_controller import login
from src.db.session import get_db

router = APIRouter()

@router.post("/login")
def login_user(email: str, password: str, db: Session = Depends(get_db)):
    return login(email, password, db)
