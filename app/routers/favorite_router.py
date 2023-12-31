from typing import List
from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.controllers.favorite_controller import add_favorite_controller
from app.models.favorite import FavoriteModel
from app.scripts.database.setup import get_db
from sqlalchemy.orm import Session
from app.utils.jwt_handler import  verify_token , verify_session


auth_scheme=HTTPBearer()

router = APIRouter()


@router.post("/{article_id}", response_model=FavoriteModel) 
def add_favorite(article_id : int , db : Session = Depends(get_db) , token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    # ** This will verify if the user's token is valid
    verify_token(token.credentials, 'user')
    return add_favorite_controller(token.credentials , article_id, db)











