from pydantic import BaseModel

class ArticleModel(BaseModel):
    #id: int | None
    url: str | None
    title: str
    abstract : str
    content : str
    authors : str
    institues: str
    references: str