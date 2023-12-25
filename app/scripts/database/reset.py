from app.config.creds import DATABASE_URL

from sqlalchemy import create_engine, MetaData

engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

for table in reversed(metadata.sorted_tables):
    table.drop(engine)

print('All tables dropped successfully!')
