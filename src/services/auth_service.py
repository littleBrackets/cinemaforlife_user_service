from sqlalchemy.orm import Session
from src.services.user_service import get_user_by_email
from src.utils.auth_util import verify_password, create_access_token

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def login_user(user_email: str):
    return create_access_token(subject=user_email)
