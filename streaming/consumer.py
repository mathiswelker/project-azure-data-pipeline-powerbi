from kafka import KafkaConsumer
import psycopg2
import json

# consumer Initialisierung
consumer = KafkaConsumer(
    "orders",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="order-consumers",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("consumer started.")

# postgres Verbindung
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin"
)
cursor = conn.cursor()

# Nachrichten verarbeiten
for message in consumer:
    order = message.value
    print(f"new message: {order}")

    # Daten in Postgres einfügen
    cursor.execute("""
        INSERT INTO orders (order_id, customer_id, product_id, quantity, total_amount, order_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        order["order_id"],
        order["customer_id"],
        order["product_id"],
        order["quantity"],
        order["total_amount"],
        order["order_date"]
    ))
    conn.commit()
