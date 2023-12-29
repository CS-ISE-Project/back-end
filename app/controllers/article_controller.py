from app.models.article import ArticleModel
from sqlalchemy.orm import Session
from app.services.article_service import create_article, get_article , update_article , delete_article
 
    
def get_article_controller(article_id: int , db : Session):
    try:
        db_article = get_article(article_id, db)
        return db_article
    except Exception as e:
        raise e
    
    
def create_article_controller(article: ArticleModel , db : Session) :
    try : 
        db_article = create_article(article , db)
        return db_article
    except Exception as e : 
        raise e
    
    
def update_article_controller(article_id : int , updated_article: ArticleModel , db : Session) : 
    try : 
        db_article = update_article(article_id, updated_article , db)
        return db_article
    except Exception as e : 
        raise e
    
    
def delete_article_controller(article_id : int , db : Session) : 
    try : 
        db_article = delete_article(article_id,db)
        return db_article
    except Exception as e : 
        raise e

