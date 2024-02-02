from typing import List, Union
from app.config.creds import INDEX_NAME

from fastapi import HTTPException, status
from app.scripts.es.setup import es

from app.models.article import ArticleModel
from app.models.query import AdvanceQueryModel
from app.models.filter import FilterModel

def get_document(document_id: int):
    document = es.get(index=INDEX_NAME, id=document_id)
    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Document with id {id} not found"
        )
    return document
    
def index_document(document_id: int, document: ArticleModel):
    try:
        res = es.index(index=INDEX_NAME, id=document_id, body=document.model_dump())
        return res
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while indexing the document. Error: {str(e)}"
        )

def delete_document(document_id: int):
    try:
        res = es.delete(index=INDEX_NAME, id=document_id)
        return res
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while deleting the document. Error: {str(e)}"
        )

def simple_query_search(query: str):
    try:
        res = es.search(
            index=INDEX_NAME,
            body={
                "query": {
                    "multi_match": {
                        "query": query,
                        "fields": ["title", "abstract", "keywords", "content", "authors", "institutes", "references"]
                    }
                }
            }
        )
        if res['hits']['total']['value'] == 0:
            return []
        return [ArticleModel(**r['_source']) for r in res['hits']['hits']]
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while performing simple search. Error: {str(e)}"
        )
    
def advanced_query_search(query: AdvanceQueryModel):
    if query.restricted:
        must_clauses = [
            {"match": {"title": query.title}} if query.title else None,
            {"match": {"keywords": query.keywords}} if query.keywords else None,
            {"match": {"content": query.content}} if query.content else None,
            {"match": {"authors": query.authors}} if query.authors else None,
            {"match": {"institutes": query.institutes}} if query.institutes else None,
        ]
        must_clauses = [clause for clause in must_clauses if clause is not None]
        try:
            res = es.search(
                index=INDEX_NAME,
                body={
                    "query": {
                        "bool" : {
                            "must" : must_clauses
                        }
                    }
                }
            )
            if res['hits']['total']['value'] == 0:
                return []
            return [ArticleModel(**r['_source']) for r in res['hits']['hits']]
        
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while performing advanced restricted search. Error: {str(e)}"
            )
    else:
        try:
            res = es.search(
                index=INDEX_NAME,
                body={
                    "query": {
                        "bool" : {
                            "should" : [
                                { "match" : {"title" : query.title} },
                                { "match" : {"keywords" : query.keywords} },
                                { "match" : {"content" : query.content} },
                                { "match" : {"authors" : query.authors} },
                                { "match" : {"institutes" : query.institutes} },
                            ]
                        }
                    }
                }
            )
            if res['hits']['total']['value'] == 0:
                return []
            return [ArticleModel(**r['_source']) for r in res['hits']['hits']]
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while performing advanced non restricted search. Error: {str(e)}"
            )

def filter_search(query: str | AdvanceQueryModel, filter: FilterModel):
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
    
    # Filtering from a simple Search
    if isinstance(query, str):
        try:
            res = es.search(
                index=INDEX_NAME,
                body={
                    "query": {
                        "bool": {
                            "must" : {
                                "multi_match": {
                                    "query": query,
                                    "fields": ["title", "abstract", "keywords", "content", "authors", "institutes", "references"]
                                }
                            },
                            "filter" : filter_clauses
                        }
                    }
                }
            )
            if res['hits']['total']['value'] == 0:
                return []
            return [ArticleModel(**r['_source']) for r in res['hits']['hits']]
        
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while filtering simple search results. Error: {str(e)}"
            )
    
    # Filtering from an Advanced Search
    elif isinstance(query, AdvanceQueryModel):
        if(query.restricted):
            must_clauses = [
                {"match": {"title": query.title}} if query.title else None,
                {"match": {"keywords": query.keywords}} if query.keywords else None,
                {"match": {"content": query.content}} if query.content else None,
                {"match": {"authors": query.authors}} if query.authors else None,
                {"match": {"institutes": query.institutes}} if query.institutes else None,
            ]
            must_clauses = [clause for clause in must_clauses if clause is not None]
            try:
                res = es.search(
                    index=INDEX_NAME,
                    body={
                        "query": {
                            "bool" : {
                                "must" : must_clauses,
                                "filter" : filter_clauses
                            }
                        }
                    }
                )
                if res['hits']['total']['value'] == 0:
                    return []
                return [ArticleModel(**r['_source']) for r in res['hits']['hits']]
            
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"An error occurred while fltering advanced restricted search results. Error: {str(e)}"
                )
        else:
            try:
                res = es.search(
                    index=INDEX_NAME,
                    body={
                        "query": {
                            "bool" : {
                                "should" : [
                                    { "match" : {"title" : query.title} },
                                    { "match" : {"keywords" : query.keywords} },
                                    { "match" : {"content" : query.content} },
                                    { "match" : {"authors" : query.authors} },
                                    { "match" : {"institutes" : query.institutes} },
                                ],
                                "filter" : filter_clauses,
                            }
                        }
                    }
                )
                if res['hits']['total']['value'] == 0:
                    return []
                return [ArticleModel(**r['_source']) for r in res['hits']['hits']]
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"An error occurred while filtering advanced non restricted search results. Error: {str(e)}"
                )
