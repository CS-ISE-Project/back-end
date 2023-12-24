from app.models.article import ArticleModel
from app.models.advanced_query import AdvanceQueryModel
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
        query={
            "multi_match": {
                "query": query,
                "fields": ["title","headline","content","authors","institutes","refrecnces"]
            }
        }
    )
    
def advance_quey_search(query : AdvanceQueryModel):
    must_clauses = [
        {"match": {"title": query.title}} if query.title else None,
        {"match": {"headline": query.headline}} if query.headline else None,
        {"match": {"content": query.content}} if query.content else None,
        {"match": {"authors": query.authors}} if query.authors else None,
        {"match": {"institutes": query.institutes}} if query.institutes else None,
    ]
    must_clauses = [clause for clause in must_clauses if clause is not None]
    print(must_clauses)
    return es.search(
        index=INDEX_NAME,
        query={
            "bool" : {
                "must" : must_clauses
            }
        }
    )
    
    
    """
    return es.search(
        index=INDEX_NAME,
        query={
            "bool" : {
                "should" : [
                    { "match" : {"title" : query.title} },
                    { "match" : {"headline" : query.headline} },
                    { "match" : {"content" : query.content} },
                    { "match" : {"authors" : query.authors} },
                    { "match" : {"institutes" : query.institutes} },
                ]
            }
        }
    )
    """