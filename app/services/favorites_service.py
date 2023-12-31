import traceback
from fastapi import Depends, HTTPException, Response , status
from sqlalchemy.orm import Session
from app.schemas.favorite import Favorite
from app.models.favorite import FavoriteModel
from app.utils.jwt_handler import decode_access_token


def add_favorite (token: str , article_id : int , db : Session) : 
    user_id = decode_access_token(token).get('id')
    db_favorite = Favorite(
        id_user = user_id,
        id_article = article_id
    )
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite
    
    
    
    
    