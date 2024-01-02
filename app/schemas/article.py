from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.schemas.base import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    title = Column(String)
    authors = Column(String)
    institues = Column(String)
    keywords = Column(String)
    abstract = Column(String)
    content = Column(String)
    references = Column(String)
    
    favorites = relationship('Favorite' , back_populates='article')