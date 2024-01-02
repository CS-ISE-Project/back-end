from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.controllers.auth_controller import signup_User_controller , login_User_controller , signup_Admin_controller , login_Admin_controller , signup_Moderator_controller , login_Moderator_controller
from app.models.user import UserModel 
from app.models.moderator import ModeratorModel  , CompleteModeratorModel , UpdateModeratorModel
from app.models.admin import AdminModel 
from app.scripts.database.setup import get_db
from sqlalchemy.orm import Session

router = APIRouter()
auth_scheme=HTTPBearer()


## ************************************* USER **********************************

@router.post("/signup", response_model=UserModel)
def create_user(user: UserModel , db : Session = Depends(get_db)):
    return signup_User_controller(user , db)


@router.post("/login")
def login(email : str , password : str , db : Session = Depends(get_db)) :
    return login_User_controller(email, password, db)


## ************************************* ADMIN **********************************


@router.post("/MYSUPERSECRETEROUTERTOADMINAUTH/signup", response_model=AdminModel)
def create_admin(admin: AdminModel , db : Session = Depends(get_db)):
    return signup_Admin_controller(admin , db)

@router.post("/MYSUPERSECRETEROUTERTOADMINAUTH/login")
def login(email : str , password : str , db : Session = Depends(get_db)) :
    return login_Admin_controller(email, password, db)


## ************************************* MODERATOR **********************************

@router.post("/MYSECRETEROUTERTOMODERATORAUTH/signup", response_model=CompleteModeratorModel)
def create_moderator(mod: ModeratorModel , db : Session = Depends(get_db)):
    return signup_Moderator_controller(mod , db)

@router.post("/MYSECRETEROUTERTOMODERATORAUTH/login")
def login(email : str , password : str , db : Session = Depends(get_db)) :
    return login_Moderator_controller(email, password, db)

