from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.controllers.auth_controller import signup_controller , login_User_controller
from app.models.user import UserModel
from app.scripts.database.setup import get_db
from sqlalchemy.orm import Session

router = APIRouter()
auth_scheme=HTTPBearer()


@router.post("/signup", response_model=UserModel)
def create_user(user: UserModel , db : Session = Depends(get_db)):
    return signup_controller(user , db)


@router.post("/loginUser")
def login(email : str , password : str , db : Session = Depends(get_db)) :
    return login_User_controller(email, password, db)