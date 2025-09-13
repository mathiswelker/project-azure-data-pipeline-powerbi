from faker import Faker
import random
from datetime import date, timedelta

fake = Faker('de_DE') 

# ---- Kunden ----
customers = []
for i in range(1, 51):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "country": "Deutschland",
        "phone": fake.phone_number(),
        "company": fake.company()
    })

# ---- Produkte ----
products = []
for i in range(1, 11): 
    products.append({
        "product_id": i,
        "name": f"Produkt {i}",
        "category": random.choice(["Elektronik", "Bücher", "Kleidung", "Lebensmittel"]),
        "price": round(random.uniform(5, 200), 2),
        "description": fake.text(max_nb_chars=100)
    })

# ---- Orders ----
orders = []
for i in range(1, 501):
    customer_id = random.randint(1, 50)
    product_id = random.randint(1, 10)
    quantity = random.randint(1, 5)
    price = products[product_id-1]["price"]

    orders.append({
        "order_id": i,
        "customer_id": customer_id,
        "product_id": product_id,
        "quantity": quantity,
        "total_amount": round(price * quantity, 2),
        "order_date": date.today() - timedelta(days=random.randint(0, 180))
    })

print("✅ Kunden, Produkte und Orders generiert")


