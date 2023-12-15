from fastapi import APIRouter
from app.controllers.user_controller import get_user_controller, create_user_controller
from app.models.user import UserModel

router = APIRouter()

@router.get("/{user_id}", response_model=UserModel)
def read_user(user_id: int):
    return get_user_controller(user_id)

@router.post("/", response_model=UserModel)
def create_user(user: UserModel):
    return create_user_controller(user)