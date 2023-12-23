from pydantic import BaseModel

class ArticleModel(BaseModel):
    title : str
    headline : str # ?
    content : str
    authors : str
    institutes : str
    refrecnces : str