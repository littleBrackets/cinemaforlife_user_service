from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.user import UserCreate
from src.utils.auth_util import get_password_hash

def create_user(db: Session, user_in: UserCreate):
    hashed_pw = get_password_hash(user_in.password)
    db_user = User(email=user_in.email, hashed_password=hashed_pw, full_name=user_in.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
