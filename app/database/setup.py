import time

from app.config.creds import DATABASE_URL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.schemas.admin import Base as AdminBase
from app.schemas.moderator import Base as ModeratorBase
from app.schemas.user import Base as UserBase
from app.schemas.article import Base as ArticleBase
from app.schemas.favorite import Base as FavoriteBase

engine = create_engine(DATABASE_URL)

AdminBase.metadata.create_all(bind=engine)
print('Admin table created!')
ModeratorBase.metadata.create_all(bind=engine)
print('Moderator table created!')   
UserBase.metadata.create_all(bind=engine)
print('User table created!')  
ArticleBase.metadata.create_all(bind=engine)
print('Article table created!')
FavoriteBase.metadata.create_all(bind=engine)
print('Favorite table created!')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print('Database setup complete!')