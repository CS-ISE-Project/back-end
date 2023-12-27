from app.models.article import ArticleModel
from app.models.advanced_query import AdvanceQueryModel
from app.services.elasticsearch_service import *

def index_document_controler(document: ArticleModel,document_id: int):
    try:
        response = index_document(document,document_id)
        return {"response ":response}
    except Exception as e:
        print("error when indexing !")
        raise e
        
def get_document_controler(document_id: int):
    try:
        response = get_document(document_id)
        return response["_source"]
    except Exception as e:
        print("error when getting !")
        raise e
    
def simple_query_search_controler(query: str):
    try:
        response = simple_query_search(query)
        return response
    except Exception as e:
        print("error when getting !")
        raise e
    
def advance_query_search_controler(query: AdvanceQueryModel):
    try:
        response = advance_quey_search(query)
        return response
    except Exception as e:
        print("error with the advance search !")
        print(e)
        raise e
    
def delete_document_controler(id_document : int):
    try:
        response = delete_document(id_document)
        return response
    except Exception as e:
        print("error while deleting")
        print(e)
        raise e