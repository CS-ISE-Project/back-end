from pydantic import BaseModel

class FavoriteModel(BaseModel):
    id_user: int
    id_article : int