from fastapi import APIRouter

from typing import List

from app.models.article import ArticleModel
from app.models.advanced_query import AdvanceQueryModel

from app.controllers.es_controller import *

router = APIRouter()

@router.get("/get_document/{document_id}",response_model=ArticleModel)
def get_document(document_id: int):
    return get_document_controller(document_id)

@router.post("/index_document/{document_id}")
def index_document(document: ArticleModel,document_id: int):
    return index_document_controller(document,document_id)

@router.post("/index_documents")
def index_multiple_documents(documents : List[ArticleModel]):
    return index_multiple_documents_controller(documents)

@router.post("/simple_search/")
def simple_query_search(query: str):
    return simple_query_search_controller(query)

@router.post("/advance_search/")
def advance_query_search(query: AdvanceQueryModel):
    return advance_query_search_controller(query)

@router.delete("/delete_document")
def delete_document(id_document : int):
    return delete_document_controller(id_document)
