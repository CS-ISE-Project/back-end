from fastapi import APIRouter, Depends
from app.controllers.article_controller import create_article_controller, get_article_controller , update_article_controller , delete_article_controller
from app.models.article import ArticleModel
from app.scripts.database.setup import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{article_id}", response_model=ArticleModel)
def read_article(article_id: int, db : Session = Depends(get_db)):
    return get_article_controller(article_id,db)

@router.post("/", response_model=ArticleModel)
def create_article(article: ArticleModel , db : Session = Depends(get_db)):
    return create_article_controller(article , db)

@router.put("/{article_id}", response_model=ArticleModel) 
def update_article(user_id: int, updated_user : ArticleModel , db : Session = Depends(get_db) ) :
    return update_article_controller(user_id, updated_user, db)


# TODO : Refactor the code so there no response body (and use the 204 status code)
@router.delete("/{article_id}" , response_model=ArticleModel )
def delete_article(article_id: int, db : Session = Depends(get_db)):
    return delete_article_controller(article_id,db)        