from sqlalchemy.orm import Session

from app.services.modification_service import add_modification, get_article_modifications, get_moderator_modifications

def add_modification_controller(token: str, article_id: int, db: Session):
    try:
        db_modification = add_modification(token, article_id, db)
        return db_modification
    except Exception as e:
        raise e

def get_article_modifications_controller(article_id: int, db: Session):
    try:
        db_modifications = get_article_modifications(article_id, db)
        return db_modifications
    except Exception as e:
        raise e
    
def get_moderator_modifications_controller(token: str, db: Session):
    try:
        db_modifications = get_moderator_modifications(token, db)
        return db_modifications
    except Exception as e:
        raise e
