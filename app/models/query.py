from pydantic import BaseModel

from app.models.filter import FilterModel

class AdvanceQueryModel(BaseModel):
    restricted: bool
    title: str
    keywords: str
    content: str
    authors: str
    institutes: str

class FilterSimpleQueryModel(BaseModel):
    query: str
    filter: FilterModel
    
class FilterAdvancedQueryModel(BaseModel):
    query: AdvanceQueryModel
    filter: FilterModel