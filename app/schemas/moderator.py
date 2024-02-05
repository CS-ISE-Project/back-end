from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.schemas.relations.base import Base

class Moderator(Base):
    __tablename__ = "moderators"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)
    is_active  = Column(Boolean, default=False)
    
    modifications = relationship('Modification' , back_populates='moderator')