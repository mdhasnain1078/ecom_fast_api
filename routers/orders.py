from fastapi import APIRouter
from schemas.order_schema import OrderIn
from models import order_model

router = APIRouter()

@router.post("/orders", status_code=201)
async def create_order(order: OrderIn):
    return await order_model.create_order(order.dict())

@router.get("/orders/{user_id}")
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    return await order_model.list_orders_by_user(user_id, limit, offset)
