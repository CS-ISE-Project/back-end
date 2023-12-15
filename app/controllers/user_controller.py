from fastapi import HTTPException
from app.models.user import User
from app.services.user_service import get_user, create_user

def get_user_controller(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def create_user_controller(user: User):
    return create_user(user)