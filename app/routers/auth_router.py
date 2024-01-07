from fastapi import APIRouter, Depends

from fastapi.security import HTTPBearer

from sqlalchemy.orm import Session
from app.scripts.database.setup import get_db

from app.models.user import UserModel 
from app.models.admin import AdminModel 
from app.models.moderator import ModeratorModel, CompleteModeratorModel

from app.controllers.auth_controller import signup_user_controller, login_user_controller, signup_admin_controller, login_admin_controller, signup_moderator_controller, login_moderator_controller

router = APIRouter()
auth_scheme=HTTPBearer()

## ************************************* USER **********************************

@router.post("/signup", response_model=UserModel)
def create_user(user: UserModel , db : Session = Depends(get_db)):
    return signup_user_controller(user , db)

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    return login_user_controller(email, password, db)

## ************************************* ADMIN **********************************

@router.post("/admin/signup", response_model=AdminModel)
def create_admin(admin: AdminModel, db: Session = Depends(get_db)):
    return signup_admin_controller(admin, db)

@router.post("/admin/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    return login_admin_controller(email, password, db)

## ************************************* MODERATOR **********************************

@router.post("/mod/signup", response_model=CompleteModeratorModel)
def create_moderator(mod: ModeratorModel, db: Session = Depends(get_db)):
    return signup_moderator_controller(mod , db)

@router.post("/mod/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    return login_moderator_controller(email, password, db)
