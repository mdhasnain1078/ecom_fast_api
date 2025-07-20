from fastapi import FastAPI
from routers import products, orders
from db.mongodb import connect_db
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

# Register Routers
app.include_router(products.router)
app.include_router(orders.router)

@app.on_event("startup")
async def startup_event():
    await connect_db()
