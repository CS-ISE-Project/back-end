from pydantic import BaseModel

class FavoriteModel(BaseModel):
    id: int | None
    id_user: int
    id_article : int