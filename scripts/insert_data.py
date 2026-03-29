import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Povezava na bazo
conn = psycopg2.connect(
    dbname="ship",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Funkcija za bulk insert
def insert_df(df, table, columns, conflict_col=None):
    tuples = [tuple(x) for x in df[columns].to_numpy()]
    if conflict_col:
        update_columns = [c for c in columns if c != conflict_col]
        query = f"""
        INSERT INTO {table} ({', '.join(columns)})
        VALUES %s
        ON CONFLICT ({conflict_col}) DO UPDATE
        SET {', '.join([f"{c} = EXCLUDED.{c}" for c in update_columns])}
        """
    else:
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES %s ON CONFLICT DO NOTHING"
    execute_values(cur, query, tuples)
    conn.commit()
    print(f"Inserted/Updated {len(df)} rows into {table}")

# --- 0. Preberi CSV ship in pripravi numeric stolpce ---
ship_df = pd.read_csv("data/ship.csv")
ship_df['mmsi'] = ship_df['mmsi'].fillna('')
ship_df['call_sign'] = ship_df['call_sign'].fillna('')
for col in ['length', 'width', 'gross_tonnage']:
    ship_df[col] = pd.to_numeric(ship_df[col], errors='coerce')  # neveljavne vrednosti -> NaN

# --- 1. Status ---
status_df = pd.read_csv("data\\status.csv")
insert_df(status_df, "dim_status", ["status_name"])

# --- 2. Ship Type ---
# --- 2. Ship Type ---
ship_type_df = pd.read_csv("data/ship_type.csv")
insert_df(ship_type_df, "dim_ship_type", ["type_name", "description"], conflict_col="ship_type_id")

# --- 3. Country ---
country_df = pd.read_csv("data\\country.csv")
insert_df(country_df, "dim_country", ["country_name", "iso_code", "region"])

# --- 4. Port ---
port_df = pd.read_csv("data\\port.csv")
insert_df(port_df, "dim_port", ["port_name", "country_id", "latitude", "longitude"])

# --- 5. Cargo Type ---
cargo_df = pd.read_csv("data\\cargo_type.csv")
insert_df(cargo_df, "dim_cargo_type", ["cargo_name", "cargo_detailed_name", "hazardous"])

# --- 6. Ship ---
insert_df(ship_df, "dim_ship", ["ship_name", "imo_number", "mmsi", "call_sign",
                                "length", "width", "gross_tonnage", "ship_type_id"])

# --- 7. Visit ---
visit_df = pd.read_csv("data\\visit.csv")
insert_df(visit_df, "fact_visit", ["ship_id", "port_id", "ETA", "ATA", "ETD", "ATD",
                                   "status_id", "cargo_type_id"])

cur.close()
conn.close()
print("Vsi CSV-ji so uvoženi v bazo!")