import pandas as pd
import random
import os
from faker import Faker
from datetime import datetime, timedelta

# Init Faker (für Fake-Namen und Adressen)
fake = Faker()

# Set output directory
OUTPUT_DIR = os.path.join("data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

customers = []
for i in range(1, 51):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address()
    })
df_customers = pd.DataFrame(customers)
df_customers.to_csv(os.path.join(OUTPUT_DIR, "customers.csv"), index=False)


# ---- Products ----
products = []
for i in range(1, 11):
    products.append({
        "product_id": i,
        "name": f"Product {i}",
        "category": random.choice(["Electronics", "Books", "Clothing", "Food"]),
        "price": round(random.uniform(5, 200), 2)
    })
df_products = pd.DataFrame(products)
df_products.to_csv(os.path.join(OUTPUT_DIR, "products.csv"), index=False)

# ---- Orders ----
orders = []
for i in range(1, 501):
    customer_id = random.randint(1, 50)
    product_id = random.randint(1, 10)
    quantity = random.randint(1, 5)
    price = df_products.loc[df_products["product_id"] == product_id, "price"].values[0]
    total = round(price * quantity, 2)
    order_date = datetime.now() - timedelta(days=random.randint(0, 180))

    orders.append({
        "order_id": i,
        "customer_id": customer_id,
        "product_id": product_id,
        "quantity": quantity,
        "total_amount": total,
        "order_date": order_date.strftime("%Y-%m-%d")
    })
df_orders = pd.DataFrame(orders)
df_orders.to_csv(os.path.join(OUTPUT_DIR, "orders.csv"), index=False)

print("✅ Dummy data generated in /data folder")
