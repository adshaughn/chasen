import sqlite3

class TeaInventory:
    def __init__(self, db_path = "data/chasen.db"):
        self.dbpath = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_stock_table()
        print("TeaInventory starting...")

    def create_stock_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                type TEXT,
                subtype TEXT,
                source TEXT,
                recommended_amount_tea REAL,
                recommended_water_ml  REAL,
                recommended_water_temp INTEGER,
                recommended_time_secs INTEGER,
                current_stock INTEGER
                );
            """)
        self.conn.commit()
        print("TeaInventory table created")