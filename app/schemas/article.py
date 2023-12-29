from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.schemas.base import Base

#Base = declarative_base()

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    title = Column(String)
    authors = Column(String)
    institues = Column(String)
    keywords = Column(String)
    abstract = Column(String)
    permissions = Column(String)
    content = Column(String)
    references = Column(String)
    
    #favorites = relationship('Favorite')