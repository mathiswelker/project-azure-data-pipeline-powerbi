import pandas as pd
from sqlalchemy import create_engine
import os

# Pfad zu CSVs
DATA_DIR = os.path.join("data")

# Postgres Verbindung
engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/postgres')

# CSVs laden
df_customers = pd.read_csv(os.path.join(DATA_DIR, "customers.csv"))
df_products  = pd.read_csv(os.path.join(DATA_DIR, "products.csv"))
df_orders    = pd.read_csv(os.path.join(DATA_DIR, "orders.csv"))

# Daten in DB schreiben
df_customers.to_sql('customers', engine, if_exists='replace', index=False)
df_products.to_sql('products', engine, if_exists='replace', index=False)
df_orders.to_sql('orders', engine, if_exists='replace', index=False)

print("✅ All CSVs loaded into Postgres!")
