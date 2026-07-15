from fastapi import APIRouter
from schemas import InventoryCreate

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.post("/add")
def add_inventory(item: InventoryCreate):
    return {
        "message": "Inventory Added Successfully",
        "data": item
    }

@router.get("/")
def get_inventory():
    return {
        "message": "Inventory List"
    }