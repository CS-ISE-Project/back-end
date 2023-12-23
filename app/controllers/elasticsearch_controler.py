from app.models.article import ArticleModel
from app.services.elasticsearch_service import *

def index_document_controler(document: ArticleModel):
    try:
        response = index_document(document)
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