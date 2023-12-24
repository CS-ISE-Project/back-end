from app.models.article import ArticleModel
from app.config.creds import INDEX_NAME
from elasticsearch import Elasticsearch
from app.elasticsearch.setup import es

def get_document(document_id: int):
    return es.get(index=INDEX_NAME, id=document_id)
    
        
def index_document(document: ArticleModel):
    return es.index(index=INDEX_NAME,id=2, body=document.dict())
