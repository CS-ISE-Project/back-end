from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    
    id_user = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='favorites')    
    
    id_article = Column(Integer, ForeignKey('articles.id'))
    article = relationship('Article' , back_populates = 'favorites')