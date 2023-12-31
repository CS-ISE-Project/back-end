from typing import List, Dict

from pydantic import BaseModel

class ArticleModel(BaseModel):
    id: int | None
    url: str
    title: str
    authors : List[str]
    institues: List[str]
    keywords: List[str]
    abstract : str
    content : str
    references: List[str]
    
class ArticlePDF(BaseModel):
    info: Dict[str, str | List[str]]
    sections: Dict[str, str]
    references: List[str]