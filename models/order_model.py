from db.mongodb import db
from bson import ObjectId

async def create_order(order: dict):
    result = await db.orders.insert_one(order)
    created = await db.orders.find_one({"_id": result.inserted_id})
    
    created["id"] = str(created["_id"])
    del created["_id"]
    
    return {'id':created["id"]}



async def list_orders_by_user(user_id: str, limit: int, offset: int):
    cursor = db.orders.find({'userId': user_id}).skip(offset).limit(limit)
    orders = []

    async for order in cursor:
        order_id = str(order["_id"])
        items = []
        total = 0.0

        for item in order["items"]:
            product_id = item["productId"]
            qty = int(item["qty"])

            product = await db.products.find_one({"_id": ObjectId(product_id)})
            if product:
                product_name = product["name"]
                product_price = float(product["price"])
                total += qty * product_price
                item_obj = {
                    "productDetails": {
                        "id": str(product["_id"]),
                        "name": product_name
                    },
                    "qty": qty
                }
                items.append(item_obj)

        orders.append({
            "id": order_id,
            "items": items,
            "total": total
        })

    next_offset = offset + limit
    prev_offset = max(0, offset - limit)

    return {
        "data": orders,
        "page": {
            "limit": limit,
            "next": next_offset,
            "previous": prev_offset
        }
    }