from fastapi import Depends, HTTPException

from sqlalchemy.orm import Session

from app.schemas.article import Article
from app.models.article import ArticleModel

def get_article(article_id: int , db: Session):
    return db.query(Article).filter(Article.id == article_id).first()

def create_article(article: ArticleModel, db: Session) :
    db_article = Article(
        title = article.title,
        url = article.url,
        authors = article.authors,
        institues = article.institues,
        keywords = article.keywords,
        abstract = article.abstract,
        content = article.content,
        references = article.references
    )
    
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def update_article(article_id: int, updated_article: ArticleModel, db: Session): 
    db_article = db.query(Article).filter(Article.id == article_id).first()
    
    db_article.title=updated_article.title,
    db_article.url = updated_article.url
    db_article.authors = updated_article.authors,
    db_article.institues = updated_article.institues,
    db_article.keywords = updated_article.keywords,
    db_article.abstract=updated_article.abstract,
    db_article.content = updated_article.content,
    db_article.references = updated_article.references,
    
    db.commit()
    db.refresh(db_article)
    return db_article

def delete_article(article_id : int , db : Session) :
    db_article = db.query(Article).filter(Article.id == article_id).first()
    
    db.delete(db_article)
    db.commit()
    return db_article