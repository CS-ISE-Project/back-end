from fastapi import APIRouter, Depends

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.utils.jwt import verify_token

from sqlalchemy.orm import Session
from app.scripts.database.setup import get_db

from app.models.modification import ModificationModel

from app.controllers.modification_controller import add_modification_controller, get_article_modifications_controller, get_moderator_modifications_controller

auth_scheme=HTTPBearer()
router = APIRouter()

@router.get("/moderator", response_model=list[ModificationModel])
def get_moderator_modifications(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, 'moderator')
    return get_moderator_modifications_controller(token.credentials, db)

@router.get("/article/{article_id}", response_model=list[ModificationModel])
def get_article_modifications(article_id: int, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, ['user', 'moderator', 'admin'])
    return get_article_modifications_controller(article_id, db)

@router.post("/{article_id}", response_model=ModificationModel)
def add_modification(article_id: int, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, 'moderator')
    return add_modification_controller(token.credentials, article_id, db)
