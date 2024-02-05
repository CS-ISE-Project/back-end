from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.schemas.relations.base import Base 

from app.schemas.user import User
from app.schemas.article import Article

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey(User.__table__.c.id))
    id_article = Column(Integer, ForeignKey(Article.__table__.c.id))
    
    user = relationship('User' , back_populates='favorites')    
    article = relationship('Article', back_populates='favorites')