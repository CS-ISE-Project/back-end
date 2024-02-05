from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.schemas.relations.base import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    publication_date = Column(Date)
    title = Column(String)
    authors = Column(String)
    institutes = Column(String)
    keywords = Column(String)
    abstract = Column(String)
    content = Column(String)
    references = Column(String)
    
    favorites = relationship('Favorite' , back_populates='article')
    modifications = relationship('Modification' , back_populates='article')
