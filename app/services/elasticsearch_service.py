from app.models.article import ArticleModel
from app.config.creds import INDEX_NAME
from elasticsearch import Elasticsearch
from app.elasticsearch.setup import get_es_instance

def get_document(document_id: int,es : Elasticsearch = get_es_instance()):
    response = es.get(index=INDEX_NAME, id=document_id)
    es.transport.close()
    return response
    
        
def index_document(document: ArticleModel,es : Elasticsearch = get_es_instance()):
    response =  es.index(index=INDEX_NAME,id=1, body=document.dict())
    es.transport.close()
    return response