from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from datetime import date
from app.utils.time import get_current_time
from app.utils.text import get_date_string, get_time_string

from app.schemas.modification import Modification

from app.utils.jwt import decode_access_token, verify_session

def get_article_modifications(article_id: int, db: Session):
    try:
        modifications = db.query(Modification).filter(Modification.id_article == article_id).all()
        if not modifications:
            # raise HTTPException(
            #     status_code=status.HTTP_404_NOT_FOUND,
            #     detail="No modifications found"
            # )
            return []
        for modification in modifications:
            modification.date = get_date_string(modification.date)
            modification.time = get_time_string(modification.time)
        return modifications
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while getting the modifications. Error: {str(e)}"
        )

def get_moderator_modifications(token: str, db: Session):
    try:
        id_moderator = decode_access_token(token).get('id')
        verify_session(token, id_moderator)
        modifications = db.query(Modification).filter(Modification.id_moderator == id_moderator).all()
        if not modifications:
            # raise HTTPException(
            #     status_code=status.HTTP_404_NOT_FOUND,
            #     detail="No modifications found"
            # )
            return []
        for modification in modifications:
            modification.date = get_date_string(modification.date)
            modification.time = get_time_string(modification.time)
        return modifications
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while getting the modifications. Error: {str(e)}"
        )

def add_modification(token: str, article_id: int, db: Session):
    try:
        id_moderator = decode_access_token(token).get('id')
        db_modification = Modification(
            id_moderator = id_moderator,
            id_article = article_id,
            date = get_date_string(date.today()),
            time = get_current_time()
        )
        verify_session(token, db_modification.id_moderator)
        db.add(db_modification)
        db.commit()
        db.refresh(db_modification)
        return db_modification
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the modification. Error: {str(e)}"
        )
