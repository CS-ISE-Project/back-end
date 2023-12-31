from fastapi import APIRouter, Depends
from app.controllers.auth_controller import signup_controller , login_controller
from app.models.user import UserModel
from app.scripts.database.setup import get_db
from sqlalchemy.orm import Session

router = APIRouter()

router = APIRouter()


@router.post("/signup", response_model=UserModel)
def create_user(user: UserModel , db : Session = Depends(get_db)):
    return signup_controller(user , db)


@router.post("/login")
def login(email : str , password : str , db : Session = Depends(get_db)) :
    return login_controller(email, password, db)