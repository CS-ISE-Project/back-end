from fastapi import APIRouter, Depends

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.utils.jwt import verify_token

from sqlalchemy.orm import Session
from app.scripts.database.setup import get_db

from typing import List
from app.models.article import ArticleModel, CompleteArticleModel

from app.controllers.article_controller import get_article_controller, create_article_controller, create_uploaded_article_controller, update_article_controller, delete_article_controller, get_all_articles_controller

auth_scheme=HTTPBearer()
router = APIRouter()

@router.get("/", response_model=List[CompleteArticleModel])
def read_all_articles(db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, ['moderator', 'admin'])
    return get_all_articles_controller(db)

@router.get("/{article_id}", response_model=CompleteArticleModel)
def read_article(article_id: int, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, ['user', 'moderator', 'admin'])
    return get_article_controller(article_id, db)

@router.post("/", response_model=CompleteArticleModel)
def create_article(article: ArticleModel, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, ['admin'])
    return create_article_controller(article, db)

@router.post("/uploaded", response_model=CompleteArticleModel)
def create_uploaded_article(article_key: str, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, ['admin'])
    return create_uploaded_article_controller(article_key, db)

@router.put("/{article_id}", response_model=CompleteArticleModel) 
def update_article(article_id: int, updated_article: ArticleModel, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, ['moderator'])
    return update_article_controller(article_id, updated_article, db)

@router.delete("/{article_id}" , response_model=CompleteArticleModel)
def delete_article(article_id: int, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, ['moderator'])
    return delete_article_controller(article_id, db)
