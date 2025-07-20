from pydantic import BaseModel
from typing import List, Optional

class ProductIn(BaseModel):
    name: str
    price: float
    sizes: List[str]

class ProductOut(ProductIn):
    id: str
