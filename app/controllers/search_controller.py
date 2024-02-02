from app.models.query import AdvanceQueryModel, FilterSimpleQueryModel, FilterAdvancedQueryModel

from app.services.es_service import simple_query_search, advanced_query_search, filter_simple_search, filter_advanced_search

def simple_search_controller(query: str):
    try:
        return simple_query_search(query)
    except Exception as e:
        raise e
    
def simple_filtered_search_controller(filter_query: FilterSimpleQueryModel):
    try:
        return filter_simple_search(query=filter_query.query, filter=filter_query.filter)
    except Exception as e:
        raise e
    
def advanced_search_controller(query: AdvanceQueryModel):
    try:
        return advanced_query_search(query)
    except Exception as e:
        raise e
    
def advanced_filtered_search_controller(filter_query: FilterAdvancedQueryModel):
    try:
        return filter_advanced_search(query=filter_query.query, filter=filter_query.filter)
    except Exception as e:
        raise e
