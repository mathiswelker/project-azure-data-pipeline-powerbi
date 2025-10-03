import requests
from sqlalchemy import create_engine
import pandas as pd
import time

# Wait for API to be ready
time.sleep(10)

# Fetch data from API endpoints
customers_resp = requests.get("http://api:5000/customers")
products_resp  = requests.get("http://api:5000/products")
orders_resp    = requests.get("http://api:5000/orders")

customers = customers_resp.json()
products  = products_resp.json()
orders    = orders_resp.json()

# Convert to DataFrames
df_customers = pd.DataFrame(customers)
df_products  = pd.DataFrame(products)
df_orders    = pd.DataFrame(orders)

# Connect to PostgreSQL and import data
engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres:5432/postgres')
try:
    df_customers.to_sql('customers', engine, if_exists='append', index=False)
    df_products.to_sql('products', engine, if_exists='append', index=False)
    df_orders.to_sql('orders', engine, if_exists='append', index=False)
    print("Data imported to Postgres")
except Exception as e:
    print(f"Failed to import API data into Postgres: {e}")
