from fastapi import HTTPException, Response, status

from sqlalchemy.orm import Session

from app.schemas.favorite import Favorite

from app.utils.jwt import decode_access_token, verify_session

def add_favorite(token: str, article_id: int, db: Session):
    try:
        id_user = decode_access_token(token).get('id')
        db_favorite = Favorite(
            id_user = id_user,
            id_article = article_id
        )
        verify_session(token, db_favorite.id_user)
        db.add(db_favorite)
        db.commit()
        db.refresh(db_favorite)
        return db_favorite
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the favorite. Error: {str(e)}"
        )

def delete_favorite(token: str, favorite_id: int, db: Session) :
    db_favorite = db.query(Favorite).filter(Favorite.id == favorite_id).first()

    if db_favorite is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Favorite with id {favorite_id} not found"
        )
        
    try:
        verify_session(token, db_favorite.id_user)
        db.delete(db_favorite)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the user. Error: {str(e)}"
        )

def get_user_favorites(token: str, db: Session):
    try:
        id_user = decode_access_token(token).get('id')
        verify_session(token, id_user)
        favorites = db.query(Favorite).filter(Favorite.id_user == id_user).all()
        if not favorites:
        #     raise HTTPException(
        #         status_code=status.HTTP_404_NOT_FOUND,
        #         detail="No favorites found"
        #     )
            return []
        return [favorite.id_article for favorite in favorites]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while getting the favorites. Error: {str(e)}"
        )
