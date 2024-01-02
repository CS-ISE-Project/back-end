from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.schemas.user import User
from app.schemas.article import Article

from sqlalchemy.ext.declarative import declarative_base
from app.schemas.base import Base

#Base = declarative_base()

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey(User.__table__.c.id))
    id_article = Column(Integer, ForeignKey(Article.__table__.c.id))
    
    user = relationship('User')
    #article = relationship('Article', back_populates='favorites')