from app.config.creds import INDEX_NAME

from typing import List

from app.scripts.es.setup import es

from app.models.article import ArticleModel
from app.models.advanced_query import AdvanceSearchModel
from app.models.filter import FilterModel

def get_document(document_id: int):
    return es.get(index=INDEX_NAME, id=document_id)
    
def index_document(document: ArticleModel, document_id: int):
    return es.index(index=INDEX_NAME,id=document_id, body=document.model_dump())

def simple_query_search(query: str):
    return es.search(
        index=INDEX_NAME,
        query={
            "multi_match": {
                "query": query,
                "fields": ["title","authors","institues","keywords","abstract","content","references"]
            }
        }
    )
    
def advance_quey_search(query: AdvanceQueryModel):
    if(query.restricted):
        must_clauses = [
            {"match": {"title": query.title}} if query.title else None,
            {"match": {"keywords": query.keywords }} if query.keywords else None,
            {"match": {"content": query.content}} if query.content else None,
            {"match": {"authors": query.authors}} if query.authors else None,
        ]
        must_clauses = [clause for clause in must_clauses if clause is not None]
        return es.search(
            index=INDEX_NAME,
            query={
                "bool" : {
                    "must" : must_clauses
                }
            }
        )
    else:
        return es.search(
            index=INDEX_NAME,
            query={
                "bool" : {
                    "should" : [
                        { "match" : {"title" : query.title} },
                        { "match" : {"keywords" : query.keywords} },
                        { "match" : {"content" : query.content} },
                        { "match" : {"authors" : query.authors} },
                    ]
                }
            }
        )
        
def delete_document(id_document: int):
    return es.delete(index=INDEX_NAME,id=id_document)

def index_multiple_documents(documents: List[ArticleModel]):
    responses = []
    for doc in documents:
        response = es.index(index=INDEX_NAME,document=doc.model_dump())
        responses.append(response)
    return responses

def filter_search(search : str|AdvanceSearchModel , filter : FilterModel):
    filter_clauses = [
            {"terms": {"authors": filter.authors}} if filter.authors else None,
            {"terms": {"keywords": filter.keywords}} if filter.keywords else None,
            {"terms": {"institues": filter.institues}} if filter.institues else None,
            {"range": {
                "dateField": {
                    "gte": filter.date_interval[0],
                    "lt": filter.date_interval[1]
                    }
                }
            } if filter.date_interval else None
        ]
    filter_clauses = [clause for clause in filter_clauses if clause is not None]
    if isinstance(search,str):
        query={
                "bool": {
                    "must" : {
                        "multi_match": {
                            "query": search,
                            "fields": ["title","authors","institues","keywords","abstract","content","references"]
                        }
                    },
                    "filter" : filter_clauses
                }
                    
        }
    elif isinstance(search,AdvanceSearchModel):
        if(query.restricted):
            must_clauses = [
                {"match": {"title": query.title}} if query.title else None,
                {"match": {"keywords": query.keywords }} if query.keywords else None,
                {"match": {"content": query.content}} if query.content else None,
                {"match": {"authors": query.authors}} if query.authors else None,
            ]
            must_clauses = [clause for clause in must_clauses if clause is not None]
            return es.search(
                index=INDEX_NAME,
                query={
                    "bool" : {
                        "must" : must_clauses,
                        "filter" : filter_clauses
                    }
                }
            )
        else:
            query={
                "bool" : {
                    "should" : [
                        { "match" : {"title" : query.title} },
                        { "match" : {"keywords" : query.keywords} },
                        { "match" : {"content" : query.content} },
                        { "match" : {"authors" : query.authors} },
                    ],
                    "filter" : filter_clauses
                }
            }
    return es.search(
        index=INDEX_NAME,
        query=query 
    )        
