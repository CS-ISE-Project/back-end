from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.schemas.base import Base

#Base = declarative_base()

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True , nullable=True)
    title = Column(String, index=True)
    abstract = Column(String, index=True)
    content = Column(String, index=True)
    authors = Column(String, index=True)
    institues = Column(String, index=True)
    references = Column(String, index=True)
    
    #favorites = relationship('Favorite')