from app.models.favorite import FavoriteModel 
from sqlalchemy.orm import Session
from app.services.favorites_service import add_favorite


def add_favorite_controller(token : str , article_id : int , db : Session):
    try:
        db_favorite = add_favorite(token, article_id, db)
        return db_favorite
    except Exception as e:
        raise e