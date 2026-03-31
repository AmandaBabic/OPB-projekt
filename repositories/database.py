import psycopg2
from repositories.database_config import *

class Database: #sem raje kopirala da se ne bo kaj uničlo zdaj na koncu
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port="5432"
        )

    def close(self):
        self.conn.close()