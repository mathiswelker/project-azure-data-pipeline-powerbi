from faker import Faker
import random
from datetime import date, timedelta

fake = Faker('de_DE') 

# Kunden generieren
def generate_customer(customer_id: int):
    return {
        "customer_id": customer_id,
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "country": "Deutschland",
        "phone": fake.phone_number(),
        "company": fake.company()
    }

# Produkte generieren
def generate_product(product_id: int):
    return {
        "product_id": product_id,
        "name": f"Produkt {product_id}",
        "category": random.choice(["Elektronik", "Bücher", "Kleidung", "Lebensmittel"]),
        "price": round(random.uniform(5, 200), 2),
        "description": fake.text(max_nb_chars=100)
    }

# Orders generieren
def generate_order(order_id: int):
    customer_id = random.randint(1, 50)
    product_id = random.randint(1, 10)
    quantity = random.randint(1, 5)
    price = round(random.uniform(5, 200), 2)
    return {
        "order_id": order_id,
        "customer_id": customer_id,
        "product_id": product_id,
        "quantity": quantity,
        "total_amount": round(price * quantity, 2),
        "order_date": (date.today() - timedelta(days=random.randint(0, 180))).isoformat()
    }
