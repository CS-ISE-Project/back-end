from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.schemas.base import Base 

#Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    
    
    # ! here is the problem, but removing it will strip the
    # ! the possibility of basculating between the tables.
    favorites = relationship('Favorite')