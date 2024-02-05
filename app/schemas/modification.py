from sqlalchemy import Column, Integer, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from app.schemas.relations.base import Base

from app.schemas.moderator import Moderator
from app.schemas.article import Article

class Modification(Base):
    __tablename__ = "modifications"

    id = Column(Integer, primary_key=True, index=True)
    id_moderator = Column(Integer, ForeignKey(Moderator.__table__.c.id))
    id_article = Column(Integer, ForeignKey(Article.__table__.c.id))
    date = Column(Date)
    time = Column(Time)
    
    moderator = relationship('Moderator' , back_populates='modifications')
    article = relationship('Article', back_populates='modifications')
