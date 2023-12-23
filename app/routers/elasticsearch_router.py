from fastapi import APIRouter,Depends
from app.controllers.elasticsearch_controler import *
from app.models.article import ArticleModel

router = APIRouter()

@router.get("/get_document/{document_id}",response_model=ArticleModel)
def get_document(document_id: int):
    return get_document_controler(document_id)

@router.post("/index_document")
def index_document(document: ArticleModel):
    return index_document_controler(document)