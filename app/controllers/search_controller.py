from app.models.query import AdvanceQueryModel

from app.services.es_service import simple_query_search, advanced_query_search

def simple_search_controller(query: str):
    try:
        return simple_query_search(query)
    except Exception as e:
        raise e
    
def advanced_search_controller(query: AdvanceQueryModel):
    try:
        return advanced_query_search(query)
    except Exception as e:
        raise e