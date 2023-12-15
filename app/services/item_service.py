from sqlalchemy.orm import Session
from app.models.item import Item
from app.core.database import SessionLocal

def get_item(item_id: int):
    db = SessionLocal()
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(item: Item):
    db = SessionLocal()
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item