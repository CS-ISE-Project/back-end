from app.config.creds import DATABASE_URL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.schemas.user import User
from app.schemas.article import Article
from app.schemas.favorite import Favorite
from app.schemas.relations.favorite import Base 

from app.schemas.admin import Base as AdminBase
from app.schemas.moderator import Base as ModeratorBase

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine, tables=[User.__table__, Article.__table__, Favorite.__table__])
print('Favorite, User and Article table created!')

AdminBase.metadata.create_all(bind=engine)
print('Admin table created!')

ModeratorBase.metadata.create_all(bind=engine)
print('Moderator table created!')   

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

print('Database setup complete!')