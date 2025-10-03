from faker import Faker
import random
from datetime import date, timedelta
import uuid

fake = Faker('de_DE')

customers = [
    {
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "country": "Deutschland",
        "phone": fake.phone_number(),
        "company": fake.company()
    }
    for i in range(1, 51)
]

products = [
    {"product_id": 1, "name": "Smartphone", "category": "Elektronik", "price": 699.99},
    {"product_id": 2, "name": "Laptop", "category": "Elektronik", "price": 1299.99},
    {"product_id": 3, "name": "Buch: Python Basics", "category": "Bücher", "price": 29.99},
    {"product_id": 4, "name": "Jeans", "category": "Kleidung", "price": 59.99},
    {"product_id": 5, "name": "T-Shirt", "category": "Kleidung", "price": 19.99},
    {"product_id": 6, "name": "Schokolade", "category": "Lebensmittel", "price": 4.99},
    {"product_id": 7, "name": "Kaffee", "category": "Lebensmittel", "price": 7.99},
    {"product_id": 8, "name": "Kopfhörer", "category": "Elektronik", "price": 199.99},
    {"product_id": 9, "name": "Notizbuch", "category": "Bücher", "price": 9.99},
    {"product_id": 10, "name": "Jacke", "category": "Kleidung", "price": 89.99}
]

orders = []
for i in range(1, 501):
    customer_id = random.randint(1, 50)
    product = random.choice(products)
    quantity = random.randint(1, 5)
    
    orders.append({
        "order_id": str(uuid.uuid4()),
        "customer_id": customer_id,
        "product_id": product["product_id"],
        "quantity": quantity,
        "total_amount": round(product["price"] * quantity, 2),
        "order_date": date.today() - timedelta(days=random.randint(0, 30))
    })

print("tables generated")