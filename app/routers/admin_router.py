from fastapi import APIRouter, Depends
from typing import List
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.controllers.admin_controller import get_admin_controller , get_all_admins_controller , create_admin_controller , update_admin_controller , delete_admin_controller
from app.models.admin import AdminModel , CompleteAdminModel , UpdateAdminModel
from app.scripts.database.setup import get_db
from sqlalchemy.orm import Session
from app.utils.jwt_handler import  verify_token , verify_session


auth_scheme=HTTPBearer()

router = APIRouter()


@router.get("/", response_model=List[CompleteAdminModel] )
def read_all_admin( db : Session = Depends(get_db) , token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials , 'admin')
    return get_all_admins_controller(db)


@router.get("/{admin_id}", response_model=AdminModel)
def read_admin(admin_id: int, db : Session = Depends(get_db) , token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials , 'admin')
    return get_admin_controller(admin_id,db)


#** To create an admin, we must have an admin already logged in 
#** THAT DOES MEAN INDEED THAT WE NEED TO HARD-CREATE ONE
@router.post("/", response_model=AdminModel) 
def create_admin(admin: AdminModel , db : Session = Depends(get_db) , token: HTTPAuthorizationCredentials = Depends(auth_scheme)) :
    verify_token(token.credentials , 'admin')
    return create_admin_controller(admin, db)

@router.put("/{admin_id}", response_model=AdminModel) 
def update_admin(admin_id: int, updated_admin : AdminModel , db : Session = Depends(get_db) , token: HTTPAuthorizationCredentials = Depends(auth_scheme)) :
    verify_token(token.credentials , 'admin')
    verify_session(token.credentials,admin_id)
    return update_admin_controller(admin_id, updated_admin, db)


# TODO : Refactor the code so there no response body (and use the 204 status code)
@router.delete("/{admin_id}" , response_model=AdminModel )
def delete_admin(admin_id: int, db : Session = Depends(get_db) , token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials , 'admin')
    verify_session(token.credentials,admin_id)
    return delete_admin_controller(admin_id,db)        