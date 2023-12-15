from fastapi import APIRouter
from app.controllers.user_controller import get_user_controller, create_user_controller
from app.models.user import User

router = APIRouter()

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int):
    return get_user_controller(user_id)

@router.post("/", response_model=User)
def create_user(user: User):
    return create_user_controller(user)