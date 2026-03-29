# repositories/repository.py

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


class Database:
    def __init__(self, dbname="ship", user="postgres", password="1234", host="localhost", port="5432"):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def close(self):
        self.conn.close()


def bulk_insert(df, table_name, columns, conn):
    """Vstavi podatke iz DataFrame v PostgreSQL tabelo."""

    # 🔹 vzamemo samo stolpce, ki jih dejansko vstavljamo
    df = df[columns]

    # 🔹 NaN pretvorimo v None (Postgres NULL)
    df = df.where(pd.notnull(df), None)

    values = [tuple(x) for x in df.to_numpy()]

    cols = ', '.join(columns)

    query = f"""
    INSERT INTO {table_name} ({cols})
    VALUES %s
    ON CONFLICT DO NOTHING
    """

    cur = conn.cursor()
    execute_values(cur, query, values)
    conn.commit()
    cur.close()

    print(f"Inserted {len(values)} rows into {table_name}")


# ------------------------------
# Repositories
# ------------------------------

class ShipRepository:

    table_name = "dim_ship"
    columns = ["ship_name", "imo_number", "mmsi", "call_sign",
               "length", "width", "gross_tonnage", "ship_type_id"]

    @staticmethod
    def insert_from_csv(filename, db: Database):
        path = os.path.join(DATA_DIR, filename)
        df = pd.read_csv(path)
        bulk_insert(df, ShipRepository.table_name, ShipRepository.columns, db.conn)

    @staticmethod
    def get_all(db: Database):
        cur = db.conn.cursor()
        cur.execute("SELECT * FROM dim_ship")
        rows = cur.fetchall()
        cur.close()
        return rows


class ShipTypeRepository:

    table_name = "dim_ship_type"
    columns = ["type_name", "description"]

    @staticmethod
    def insert_from_csv(filename, db: Database):
        path = os.path.join(DATA_DIR, filename)
        df = pd.read_csv(path)
        bulk_insert(df, ShipTypeRepository.table_name, ShipTypeRepository.columns, db.conn)

    @staticmethod
    def get_all(db: Database):
        cur = db.conn.cursor()
        cur.execute("SELECT * FROM dim_ship_type")
        rows = cur.fetchall()
        cur.close()
        return rows


class CountryRepository:

    table_name = "dim_country"
    columns = ["country_name", "iso_code", "region"]

    @staticmethod
    def insert_from_csv(filename, db: Database):
        path = os.path.join(DATA_DIR, filename)
        df = pd.read_csv(path)
        bulk_insert(df, CountryRepository.table_name, CountryRepository.columns, db.conn)

    @staticmethod
    def get_all(db: Database):
        cur = db.conn.cursor()
        cur.execute("SELECT * FROM dim_country")
        rows = cur.fetchall()
        cur.close()
        return rows


class PortRepository:

    table_name = "dim_port"
    columns = ["port_name", "country_id", "latitude", "longitude"]

    @staticmethod
    def insert_from_csv(filename, db: Database):
        path = os.path.join(DATA_DIR, filename)
        df = pd.read_csv(path)
        bulk_insert(df, PortRepository.table_name, PortRepository.columns, db.conn)

    @staticmethod
    def get_all(db: Database):
        cur = db.conn.cursor()
        cur.execute("SELECT * FROM dim_port")
        rows = cur.fetchall()
        cur.close()
        return rows


class CargoTypeRepository:

    table_name = "dim_cargo_type"
    columns = ["cargo_name", "cargo_detailed_name", "hazardous"]

    @staticmethod
    def insert_from_csv(filename, db: Database):
        path = os.path.join(DATA_DIR, filename)
        df = pd.read_csv(path)
        bulk_insert(df, CargoTypeRepository.table_name, CargoTypeRepository.columns, db.conn)

    @staticmethod
    def get_all(db: Database):
        cur = db.conn.cursor()
        cur.execute("SELECT * FROM dim_cargo_type")
        rows = cur.fetchall()
        cur.close()
        return rows


class StatusRepository:

    table_name = "dim_status"
    columns = ["status_name"]

    @staticmethod
    def insert_from_csv(filename, db: Database):
        path = os.path.join(DATA_DIR, filename)
        df = pd.read_csv(path)
        bulk_insert(df, StatusRepository.table_name, StatusRepository.columns, db.conn)

    @staticmethod
    def get_all(db: Database):
        cur = db.conn.cursor()
        cur.execute("SELECT * FROM dim_status")
        rows = cur.fetchall()
        cur.close()
        return rows


class VisitRepository:

    table_name = "fact_visit"
    columns = ["ship_id", "port_id", "ETA", "ATA", "ETD", "ATD",
               "status_id", "cargo_type_id"]

    @staticmethod
    def insert_from_csv(filename, db: Database):
        path = os.path.join(DATA_DIR, filename)
        df = pd.read_csv(path)
        bulk_insert(df, VisitRepository.table_name, VisitRepository.columns, db.conn)

    @staticmethod
    def get_all(db: Database):
        cur = db.conn.cursor()
        cur.execute("SELECT * FROM fact_visit")
        rows = cur.fetchall()
        cur.close()
        return rows
    
    