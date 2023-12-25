from typing import Optional

from pydantic import BaseModel


class FavoriteModel(BaseModel):
    id: Optional[int]
    id_user: int
    id_article : int
    
