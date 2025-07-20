from fastapi import APIRouter, Query
from typing import Optional
from models import product_model
from schemas.product_schema import ProductIn

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(product: ProductIn):
    print("------------------------------------------------ Product -------------------------------------------\n",product)
    return await product_model.create_product(product.dict())

@router.get("/products")
async def list_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    filters = {}
    if name:
        filters['name'] = {'$regex': name, '$options': 'i'}
    if size:
        filters['sizes'] = size
    return await product_model.list_products(filters, limit, offset)
