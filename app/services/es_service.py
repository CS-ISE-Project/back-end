from typing import List
from app.config.creds import INDEX_NAME

from fastapi import HTTPException, status
from app.scripts.es.setup import es

from app.models.article import ArticleModel
from app.models.advanced_query import AdvanceQueryModel

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
            query={
                "multi_match": {
                    "query": query,
                    "fields": ["title","headline","content","authors","institutes","refrecnces"]
                }
            }
        )
        return res
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while searching the document. Error: {str(e)}"
        )
    
def advance_quey_search(query: AdvanceQueryModel):
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
                query={
                    "bool" : {
                        "must" : must_clauses
                    }
                }
            )
            return res
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while searching the document. Error: {str(e)}"
            )
    else:
        try:
            res = es.search(
                index=INDEX_NAME,
                query={
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
            )
            return res
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while searching the document. Error: {str(e)}"
            )
