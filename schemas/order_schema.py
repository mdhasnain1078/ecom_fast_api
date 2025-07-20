from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    productId: str
    qty: str

class OrderIn(BaseModel):
    userId: str
    items: List[Item]

class OrderOut(OrderIn):
    id: str
