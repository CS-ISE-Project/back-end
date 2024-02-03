from fastapi import APIRouter, Depends

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.utils.jwt import verify_token, verify_session

from sqlalchemy.orm import Session
from app.scripts.database.setup import get_db

from typing import List
from app.models.moderator import ModeratorModel, UpdateModeratorModel, CompleteModeratorModel

from app.controllers.moderator_controller import get_all_moderator_controller, create_moderator_controller, get_moderator_controller , update_moderator_controller , delete_moderator_controller

auth_scheme=HTTPBearer()
router = APIRouter()

@router.get("/", response_model=List[CompleteModeratorModel] )
def read_all_moderators(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials , ['moderator', 'admin'])
    return get_all_moderator_controller(db)

@router.get("/{mod_id}", response_model=CompleteModeratorModel)
def read_moderator(mod_id: int, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials,['moderator', 'admin'])
    return get_moderator_controller(mod_id,db)

@router.post("/", response_model=ModeratorModel)
def create_moderator(mod: ModeratorModel, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials,['moderator', 'admin'])
    return create_moderator_controller(mod , db)

@router.put("/{mod_id}", response_model=ModeratorModel) 
def update_moderator(mod_id: int, updated_mod: ModeratorModel, db: Session = Depends(get_db) , token: HTTPAuthorizationCredentials = Depends(auth_scheme) ) :
    verify_token(token.credentials,['moderator', 'admin'])
    verify_session(token.credentials,mod_id)
    return update_moderator_controller(mod_id, updated_mod, db)

@router.delete("/{mod_id}" , response_model=ModeratorModel )
def delete_moderator(mod_id: int, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials,['moderator', 'admin'])
    verify_session(token.credentials,mod_id)    
    return delete_moderator_controller(mod_id,db)  
