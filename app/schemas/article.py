from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.schemas.relations.favorite import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    title = Column(String)
    authors = Column(String)
    institutes = Column(String)
    keywords = Column(String)
    abstract = Column(String)
    content = Column(String)
    references = Column(String)
    
    favorites = relationship('Favorite' , back_populates='article')