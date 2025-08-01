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
                primary_type TEXT,
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


    def add_tea(self, name, primary_type, subtype, source, recommended_amount_tea, recommended_water_ml, recommended_water_temp, recommended_time_secs):
        self.cursor.execute("""
            INSERT INTO stock (
                name,
                primary_type,
                subtype,
                source,
                recommended_amount_tea,
                recommended_water_ml,
                recommended_water_temp,
                recommended_time_secs
                            ) VALUES (?,?,?,?,?,?,?,?);
                """, (name, primary_type, subtype, source, recommended_amount_tea, recommended_water_ml, recommended_water_temp, recommended_time_secs))
        self.conn.commit()
        print(f"{name} added to stock table")

    def list_teas(self):
        self.cursor.execute("""
                            SELECT
                                name,
                                primary_type,
                                recommended_amount_tea,
                                recommended_water_ml,
                                recommended_water_temp,
                                recommended_time_secs
                            FROM stock
                            """)
        teas = self.cursor.fetchall()

        if not teas:
            print("No teas in stock table")
            return

        print("Current teas in stock table:")
        for tea in teas:
            name, primary_type, recommended_amount_tea, recommended_water_ml, recommended_water_temp, recommended_time_secs = tea
            print(f" - {name} ({primary_type}) : {recommended_amount_tea}g with {recommended_water_ml}ml water at {recommended_water_temp}°C for {recommended_time_secs} sec.")