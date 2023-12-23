from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    summury = Column(String, index=True)
    url = Column(String, index=True)
    text = Column(String, index=True)
    institues = Column(String, index=True)
    authors = Column(String, index=True)
    references = Column(String, index=True)
    
    id_favorites = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship('Favorite', back_populates='article')
