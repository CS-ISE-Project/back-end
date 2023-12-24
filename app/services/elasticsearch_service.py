from app.models.article import ArticleModel
from app.config.creds import INDEX_NAME
from elasticsearch import Elasticsearch
from app.elasticsearch.setup import es

def get_document(document_id: int):
    return es.get(index=INDEX_NAME, id=document_id)
    
        
def index_document(document: ArticleModel,document_id: int):
    return es.index(index=INDEX_NAME,id=document_id, body=document.dict())

def simple_query_search(query:str):
    return es.search(
        index=INDEX_NAME,
        query=
        {
            "multi_match": {
                "query": query,
                "fields": ["summary", "title","headline","content","authors","institutes","refrecnces"]
            }
        }
    )
