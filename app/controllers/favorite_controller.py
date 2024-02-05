from sqlalchemy.orm import Session

from app.models.favorite import FavoriteModel

from app.services.favorites_service import add_favorite, delete_favorite, get_user_favorites

def add_favorite_controller(token : str , article_id : int , db : Session):
    try:
        db_favorite = add_favorite(token, article_id, db)
        return db_favorite
    except Exception as e:
        raise e

def delete_favorite_controller(token : str , favorite_id : int , db : Session):
    try:
        db_favorite = delete_favorite(token, favorite_id, db)
        return db_favorite
    except Exception as e:
        raise e

def get_user_favorites_controller(token: str, db: Session):
    try:
        db_favorites = get_user_favorites(token, db)
        return db_favorites
    except Exception as e:
        raise e
