from app.config.creds import DATABASE_URL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.schemas.admin import Base as AdminBase
from app.schemas.article import Base as ArticleBase
from app.schemas.moderator import Base as ModeratorBase
from app.schemas.favorite import Base as FavoriteBase
from app.schemas.user import Base as UserBase

engine = create_engine(DATABASE_URL)

# Declare models
AdminBase.metadata.create_all(bind=engine)
UserBase.metadata.create_all(bind=engine)  
ArticleBase.metadata.create_all(bind=engine)
ModeratorBase.metadata.create_all(bind=engine)   
FavoriteBase.metadata.create_all(bind=engine)

# Declare session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
