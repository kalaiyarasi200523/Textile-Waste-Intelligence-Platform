from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str


class InventoryCreate(BaseModel):
    waste_batch_id: str
    fabric_type: str
    source: str
    quantity: str
    color: str
    condition: str
    collection_date: str

