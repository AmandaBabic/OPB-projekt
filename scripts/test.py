# test če imajo vse tabele podatke
import pandas as pd
import psycopg2

# Povezava na bazo
conn = psycopg2.connect(
    dbname="ship",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

# test vsebine tabel
def check_table(table_name, n=5):
    df = pd.read_sql(f"SELECT * FROM {table_name} LIMIT {n};", conn)
    print(f"\n--- Prvih {n} vrstic iz {table_name} ---")
    print(df)

# --- 1. Ship ---
check_table("dim_ship")

# --- 2. Ship Type ---
check_table("dim_ship_type")

# --- 3. Country ---
check_table("dim_country")

# --- 4. Port ---
check_table("dim_port")

# --- 5. Visit ---
check_table("fact_visit")

# --- 6. Cargo Type ---
check_table("dim_cargo_type")

# --- 7. Status ---
check_table("dim_status")

# Zapremo povezavo
conn.close()