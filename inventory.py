import sqlite3


class TeaInventory:
    def __init__(self, db_path="data/chasen.db"):
        self.dbpath = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_stock_table()
        print("TeaInventory starting...")

    def create_stock_table(self):
        """Creates the table to store tea inventory data"""
        self.cursor.execute(
            """
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
            """
        )
        self.conn.commit()
        print("TeaInventory table created")

    def add_tea(
        self,
        name,
        primary_type,
        subtype,
        source,
        recommended_amount_tea,
        recommended_water_ml,
        recommended_water_temp,
        recommended_time_secs,
    ):
        """
        Adds a tea to the inventory table. First checks to see if the tea already exists (case-insensitive) and if so then adds it to
        the inventory table

        Args:
            name (str): The name of the tea
            primary_type (str): The primary type of the tea
            subtype (str): The subtype of the tea
            source (str): The source of the tea
            recommended_amount_tea (str): The recommended amount of the tea in grams
            recommended_water_ml (str): The recommended water of the tea in ml
            recommended_water_temp (str): The recommended water of the tea in celsius
            recommended_time_secs (str): The recommended steep time in seconds

        Returns:
            TODO
        """

        self.cursor.execute(
            "SELECT id FROM stock WHERE LOWER(name) = LOWER(?)", (name,)
        )
        if self.cursor.fetchone():
            print(f"{name} already exists in inventory")
            return

        self.cursor.execute(
            """
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
                """,
            (
                name,
                primary_type,
                subtype,
                source,
                recommended_amount_tea,
                recommended_water_ml,
                recommended_water_temp,
                recommended_time_secs,
            ),
        )
        self.conn.commit()
        print(f"{name} added to stock table")

    def list_teas(self):
        """Function that lists all rows in the tea inventory table (table name: stock)"""
        self.cursor.execute(
            """
                            SELECT
                                name,
                                primary_type,
                                recommended_amount_tea,
                                recommended_water_ml,
                                recommended_water_temp,
                                recommended_time_secs
                            FROM stock
                            """
        )
        teas = self.cursor.fetchall()

        if not teas:
            print("No teas in stock table")
            return

        print("Current teas in stock table:")
        for tea in teas:
            (
                name,
                primary_type,
                recommended_amount_tea,
                recommended_water_ml,
                recommended_water_temp,
                recommended_time_secs,
            ) = tea
            print(
                f" - {name} ({primary_type}) : {recommended_amount_tea}g with {recommended_water_ml}ml water at {recommended_water_temp}°C for {recommended_time_secs} sec."
            )
