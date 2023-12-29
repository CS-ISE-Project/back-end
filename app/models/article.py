from typing import List

from pydantic import BaseModel

class ArticleModel(BaseModel):
    id: int | None
    url: str
    title: str
    authors : List[str]
    institues: List[str]
    keywords: List[str]
    abstract : str
    permissions: str
    content : str
    references: List[str]
    
class ArticlePDF(BaseModel):
    pages: List[str]