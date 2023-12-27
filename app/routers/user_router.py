from fastapi import APIRouter, Depends
from app.controllers.user_controller import create_user_controller, get_user_controller
from app.models.user import UserModel
from app.scripts.database.setup import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{user_id}", response_model=UserModel)
def read_user(user_id: int, db : Session = Depends(get_db)):
    return get_user_controller(user_id,db)

@router.post("/", response_model=UserModel)
def create_user(user: UserModel):
    return create_user_controller(user)
