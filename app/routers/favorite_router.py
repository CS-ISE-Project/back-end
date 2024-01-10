from fastapi import APIRouter, Depends

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.utils.jwt import verify_token

from sqlalchemy.orm import Session
from app.scripts.database.setup import get_db

from app.models.favorite import FavoriteModel

from app.controllers.favorite_controller import add_favorite_controller, delete_favorite_controller

auth_scheme=HTTPBearer()
router = APIRouter()

@router.post("/{article_id}", response_model=FavoriteModel) 
def add_favorite(article_id: int, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, 'user')
    return add_favorite_controller(token.credentials , article_id, db)

@router.delete("/{favorite_id}", response_model=FavoriteModel) 
def delete_favorite(favorite_id: int, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, 'user')
    return delete_favorite_controller(token.credentials , favorite_id, db)
