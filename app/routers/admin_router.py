from fastapi import APIRouter, Depends

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.utils.jwt import  verify_token , verify_session

from sqlalchemy.orm import Session
from app.scripts.database.setup import get_db

from typing import List
from app.models.admin import AdminModel, CompleteAdminModel, UpdateAdminModel
from app.models.moderator import ActiveModeratorModel

from app.controllers.admin_controller import get_admin_controller, get_all_admins_controller, create_admin_controller, update_admin_controller, delete_admin_controller , activate_moderator_controller

auth_scheme = HTTPBearer()
router = APIRouter()

@router.get("/", response_model=List[CompleteAdminModel])
def read_all_admin(db: Session = Depends(get_db) , token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials , 'admin')
    return get_all_admins_controller(db)

@router.get("/{admin_id}", response_model=CompleteAdminModel)
def read_admin(admin_id: int, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials , 'admin')
    return get_admin_controller(admin_id,db)

@router.post("/", response_model=AdminModel)
def create_admin(admin: AdminModel, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)) :
    verify_token(token.credentials , 'admin')
    return create_admin_controller(admin, db)

@router.put("/{admin_id}", response_model=AdminModel) 
def update_admin(admin_id: int, updated_admin: AdminModel, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)) :
    verify_token(token.credentials , 'admin')
    verify_session(token.credentials,admin_id)
    return update_admin_controller(admin_id, updated_admin, db)

@router.delete("/{admin_id}" , response_model=AdminModel )
def delete_admin(admin_id: int, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials , 'admin')
    verify_session(token.credentials,admin_id)
    return delete_admin_controller(admin_id,db)

@router.put("/modActivate/{mod_id}", response_model=ActiveModeratorModel) 
def activate_moderator(mod_id : int, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)) :
    verify_token(token.credentials , 'admin')
    return activate_moderator_controller(mod_id, db)