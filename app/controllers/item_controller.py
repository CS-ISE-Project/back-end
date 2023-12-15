from fastapi import HTTPException
from app.models.item import Item
from app.services.item_service import get_item, create_item

def get_item_controller(item_id: int):
    item = get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

def create_item_controller(item: Item):
    return create_item(item)