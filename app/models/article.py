from typing import List

from pydantic import BaseModel

class ArticleModel(BaseModel):
    url: str
    publication_date: str
    title: str
    authors : List[str]
    institutes: List[str]
    keywords: List[str]
    abstract : str
    content : str
    references: List[str]

class CompleteArticleModel(BaseModel):
    id: int
    url: str
    publication_date: str
    title: str
    authors : List[str]
    institutes: List[str]
    keywords: List[str]
    abstract : str
    content : str
    references: List[str]
