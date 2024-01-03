from typing import List

from app.models.article import ArticleModel
from app.models.advanced_query import AdvanceQueryModel

from app.services.es_service import *

def get_document_controller(document_id: int):
    try:
        response = get_document(document_id)
        return response["_source"]
    except Exception as e:
        print(f"Error getting document with id: {id}!")
        raise e

def index_document_controller(document: ArticleModel, document_id: int):
    try:
        response = index_document(document,document_id)
        return {"response ":response}
    except Exception as e:
        print("Error indexing document!")
        raise e
        
def index_multiple_documents_controller(documents: List[ArticleModel]):
    try:
        response = index_multiple_documents(documents)
        return response
    except Exception as e:
        print("Error indexing multiple documents!")
        raise e
    
def simple_query_search_controller(query: str):
    try:
        response = simple_query_search(query)
        return response
    except Exception as e:
        print(f"Error searching for query: {query}!")
        raise e
    
def advance_query_search_controller(query: AdvanceQueryModel):
    try:
        response = advance_quey_search(query)
        return response
    except Exception as e:
        print(f"Error searching for query: {query.model_dump()}!")
        raise e
    
def delete_document_controller(id_document : int):
    try:
        response = delete_document(id_document)
        return response
    except Exception as e:
        print(f"Error deleting document with id: {id}!")
        raise e
