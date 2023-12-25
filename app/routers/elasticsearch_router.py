from fastapi import APIRouter,Depends
from app.controllers.elasticsearch_controler import *
from app.models.article import ArticleModel
from app.models.advanced_query import AdvanceQueryModel

router = APIRouter()

@router.get("/get_document/{document_id}",response_model=ArticleModel)
def get_document(document_id: int):
    return get_document_controler(document_id)

@router.post("/index_document/{document_id}")
def index_document(document: ArticleModel,document_id: int):
    return index_document_controler(document,document_id)

@router.get("/simple_query_search/")
def simple_query_search(query: str):
    return simple_query_search_controler(query)

@router.post("/advance_query_search/")
def advance_query_search(query: AdvanceQueryModel):
    return advance_query_search_controler(query)