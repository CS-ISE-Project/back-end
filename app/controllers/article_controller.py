from sqlalchemy.orm import Session

from app.models.article import ArticleModel, CompleteArticleModel

from app.services.article_loading_service import load_article
from app.services.article_service import create_article, get_article, update_article, delete_article, get_all_articles
from app.services.es_service import index_document, delete_document

from app.utils.article import db_to_model
from app.utils.upload import path_from_key, delete_pdf

def get_all_articles_controller(db: Session):
    try:
        db_articles = get_all_articles(db)
        articles = [db_to_model(db_article) for db_article in db_articles]
        return articles
    except Exception as e:
        raise e

def get_article_controller(article_id: int, db: Session):
    try:
        db_article = get_article(article_id, db)
        article = db_to_model(db_article)
        return article
    except Exception as e:
        raise e

def create_article_controller(article: ArticleModel, db: Session):
    try:
        db_article = create_article(article, db)
    except Exception as e:
        raise e
    try:
        index_document(db_article.id, article)
    except Exception as e:
        try:
            delete_article(db_article.id, db)
        except Exception as e:
            raise e
        raise e
    return db_to_model(db_article)

def create_uploaded_article_controller(article_key: str, db: Session):
    try:
        article = load_article(path_from_key(article_key))
    except Exception as e:
        raise e
    try:
        db_article = create_article(article, db)
    except Exception as e:
        raise e
    try:
        index_document(db_article.id, article)
    except Exception as e:
        try:
            delete_article(db_article.id, db)
        except Exception as e:
            raise e
        raise e
    # delete_pdf(article_key)
    return db_to_model(db_article)
    
def update_article_controller(article_id: int, updated_article: ArticleModel, db: Session): 
    try:
        backup_db_article = get_article(article_id, db)
        backup_article = db_to_model(backup_db_article, include_id=False)
    except Exception as e:
        raise e
    try:
        db_article = update_article(article_id, updated_article, db)
    except Exception as e: 
        raise e
    try:
        index_document(article_id, updated_article)
    except Exception as e:
        try:
            update_article(article_id, backup_article, db)
        except Exception as e:
            raise e
        raise e
    return db_to_model(db_article)

def delete_article_controller(article_id: int, db: Session):
    try:
        db_article = delete_article(article_id, db)
        article = db_to_model(db_article, include_id=False)
    except Exception as e:
        raise e
    try:
        delete_document(article_id)
    except Exception as e:
        try:
            create_article(article, db)
        except Exception as e:
            raise e
        raise e
    return db_to_model(db_article)
