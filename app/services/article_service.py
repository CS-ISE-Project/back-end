from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from app.schemas.article import Article
from app.models.article import ArticleModel

from app.utils.article import model_to_db
from app.utils.text import get_date

def get_all_articles(db: Session):
    articles = db.query(Article).all()
    if not articles:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No articles found"
        )
    return articles

def get_article(article_id: int , db: Session):
    article = db.query(Article).filter(Article.id == article_id).first()
    if article is None:
        raise HTTPException(
            status_code=404,
            detail=f"Article with id {article_id} not found"
        )
    return article

def create_article(article: ArticleModel, db: Session):
    try:
        article_model = model_to_db(article)
        db_article = Article(
            url = article_model.url,
            publication_date = article_model.publication_date,
            title = article_model.title,
            authors = article_model.authors,
            institutes = article_model.institutes,
            keywords = article_model.keywords,
            abstract = article_model.abstract,
            content = article_model.content,
            references = article_model.references
        )
        db.add(db_article)
        db.commit()
        db.refresh(db_article)
        return db_article
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the article. Error: {str(e)}"
        )
        
def update_article(article_id: int, updated_article: ArticleModel, db: Session): 
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if db_article is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {db_article} not found"
        )
    updated_article = model_to_db(updated_article)
    try:
        db_article.url = updated_article.url
        db_article.publication_date = updated_article.publication_date,
        db_article.title=updated_article.title,
        db_article.authors = updated_article.authors,
        db_article.institutes = updated_article.institutes,
        db_article.keywords = updated_article.keywords,
        db_article.abstract=updated_article.abstract,
        db_article.content = updated_article.content,
        db_article.references = updated_article.references,
        
        db.commit()
        db.refresh(db_article)
        return db_article
    except Exception as e :
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while updating the article. Error: {str(e)}"
        )

def delete_article(article_id: int , db: Session):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if db_article is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {db_article} not found"
        )
    try:
        db.delete(db_article)
        db.commit()
        return db_article
    except Exception as e :
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while deleting the article. Error: {str(e)}"
        )
