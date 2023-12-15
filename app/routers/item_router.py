from fastapi import APIRouter
from app.controllers.item_controller import get_item_controller, create_item_controller
from app.models.item import Item

router = APIRouter()

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int):
    return get_item_controller(item_id)

@router.post("/", response_model=Item)
def create_item(item: Item):
    return create_item_controller(item)