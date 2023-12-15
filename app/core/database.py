from app.core.creds import DATABASE_URL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.schemas.user import Base

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)