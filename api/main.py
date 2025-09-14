from fastapi import FastAPI
from routers import customers, products, orders

app = FastAPI(title="Fake Shop API")

# Router registrieren
app.include_router(customers.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "Fake Shop API is running"}
