from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime
import uuid

# Producer Initialisierung
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Liste von Produkten
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

print("producer started.")

try:
    while True:
        product = random.choice(products)
        quantity = random.randint(1, 5)
        order = {
            "order_id": str(uuid.uuid4()),
            "customer_id": random.randint(1, 50),
            "product_id": product["product_id"],
            "quantity": quantity,
            "total_amount": round(product["price"] * quantity, 2),
            "order_date": datetime.now().isoformat()
        }

        producer.send("orders", value=order)
        print(f" new order arrived: {order}")

        time.sleep(3)
except KeyboardInterrupt:
    print("producer stopped.")
