import traceback
from fastapi import Depends, HTTPException, Response , status
from sqlalchemy.orm import Session
from app.schemas.favorite import Favorite
from app.models.favorite import FavoriteModel
from app.utils.jwt_handler import decode_access_token , verify_session


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
    


def delete_favorite(token: str , favorite_id : int , db : Session ) :
    db_favorite = db.query(Favorite).filter(Favorite.id == favorite_id).first()

    if db_favorite is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {favorite_id} not found"
        )

    try:
        
        verify_session(token, db_favorite.id_user)
        db.delete(db_favorite)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    
    except Exception as e:
        db.rollback()
        trace = traceback.format_exec()
        # ! for Debug purposes
        #print("THE ERROR STACK IS : " , trace) 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the user. Error: {str(e)}"
        )    
    
    