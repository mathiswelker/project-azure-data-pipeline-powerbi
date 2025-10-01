import requests
from sqlalchemy import create_engine
import pandas as pd

customers_resp = requests.get("http://127.0.0.1:8000/customers")
products_resp  = requests.get("http://127.0.0.1:8000/products")
orders_resp    = requests.get("http://127.0.0.1:8000/orders")

customers = customers_resp.json()
products  = products_resp.json()
orders    = orders_resp.json()


df_customers = pd.DataFrame(customers)
df_products  = pd.DataFrame(products)
df_orders    = pd.DataFrame(orders)


engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/postgres')
try:
    df_customers.to_sql('customers', engine, if_exists='append', index=False)
    df_products.to_sql('products', engine, if_exists='append', index=False)
    df_orders.to_sql('orders', engine, if_exists='append', index=False)
except Exception as e:
    print(f"failed to import api-data into postgres {e}")

print("data imported to postgres")
