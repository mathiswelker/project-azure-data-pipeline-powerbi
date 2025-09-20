from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

# Producer Definition
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Liste von Fake-Produkten
products = [
    {"product_id": 1, "name": "Laptop", "price": 1200},
    {"product_id": 2, "name": "Buch", "price": 20},
    {"product_id": 3, "name": "T-Shirt", "price": 15},
    {"product_id": 4, "name": "Headphones", "price": 80}
]

print("Producer gestartet ...")

try:
    while True:
        product = random.choice(products)
        order = {
            "order_id": random.randint(1000, 9999),
            "customer_id": random.randint(1, 50),
            "product_id": product["product_id"],
            "quantity": random.randint(1, 5),
            "total_amount": product["price"] * random.randint(1, 5),
            "order_date": datetime.now().isoformat()
        }

        producer.send("orders", value=order)
        print(f"✅ Neue Order gesendet: {order}")

        time.sleep(3)
except KeyboardInterrupt:
    print("🛑 Producer gestoppt.")
