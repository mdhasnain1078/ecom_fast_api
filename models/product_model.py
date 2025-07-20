from db.mongodb import db
from bson import ObjectId

from schemas.product_schema import ProductOut

async def create_product(product: dict):
    result = await db.products.insert_one(product)
    product["id"] = str(result.inserted_id)
    # product_out = ProductOut(**product)
    # return product_out
    return {'id': product["id"]}

async def list_products(filters: dict, limit: int, offset: int):
    cursor = db.products.find(filters).skip(offset).limit(limit)
    results = []

    async for doc in cursor:
        doc['id'] = str(doc['_id'])
        del doc['_id']
        results.append(doc)

    next_offset = offset + limit
    previous_offset = max(0, offset - limit)

    return {
        "data": results,
        "page": {
            "limit": limit,
            "next": next_offset,
            "previous": previous_offset
        }
    }
