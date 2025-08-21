import sqlite3

from tabulate import tabulate


class TeaInventory:
    def __init__(self, conn=None, db_path="chasen/chasen/data/chasen.db"):
        if conn is not None:
            self.conn = conn
        else:
            self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_stock_table()
        print("TeaInventory starting...")

    def create_stock_table(self):
        """Creates the table (table name: stock) to store tea inventory data"""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                primary_type TEXT NOT NULL,
                subtype TEXT NOT NULL,
                source TEXT NOT NULL,
                recommended_amount_tea REAL NOT NULL,
                recommended_water_ml  REAL NOT NULL,
                recommended_water_temp INTEGER NOT NULL,
                recommended_time_secs INTEGER NOT NULL,
                current_stock INTEGER NOT NULL
                );
            """
        )
        self.conn.commit()
        print("TeaInventory table created")

    def delete_stock_table(self):
        """Deletes the tea inventory table (stock)"""
        self.cursor.execute("DROP TABLE stock")
        self.conn.commit()
        print("TeaInventory table deleted")

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
        current_stock,
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

        TODO modify to allow for adding quantity to existing tea
        """
        # Step 1: Make sure nothing in input is blank/null
        required_fields = {
            "name": name,
            "primary_type": primary_type,
            "recommended_amount_tea": recommended_amount_tea,
            "recommended_water_ml": recommended_water_ml,
            "recommended_water_temp": recommended_water_temp,
            "recommended_time_secs": recommended_time_secs,
            "current_stock": current_stock,
        }
        for field, value in required_fields.items():
            if value is None:
                raise ValueError(f"{field} is required and cannot be None")

        # Step 2: Check field types

        numeric_fields = {
            "recommended_amount_tea": recommended_amount_tea,
            "recommended_water_ml": recommended_water_ml,
            "recommended_water_temp": recommended_water_temp,
            "recommended_time_secs": recommended_time_secs,
            "current_stock": current_stock,
        }
        for field, value in numeric_fields.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"{field} must be numeric")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(primary_type, str) or not primary_type.strip():
            raise ValueError("primary_type must be a non-empty string")

        # Step 3: Check for duplicates

        self.cursor.execute(
            "SELECT id FROM stock WHERE LOWER(name) = LOWER(?)", (name,)
        )
        if self.cursor.fetchone():
            print(f"{name} already exists in inventory")
            return

        # Step 4: Insert new entry into stock table
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
                recommended_time_secs,
                current_stock
                            ) VALUES (?,?,?,?,?,?,?,?,?);
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
                current_stock,
            ),
        )
        self.conn.commit()
        print(f"{name} added to stock table")

    def remove_tea(self, name):
        """Removes a tea with the name selected from the inventory table"""

        self.cursor.execute(
            "SELECT id FROM stock WHERE LOWER(name) = LOWER(?)", (name,)
        )
        if not self.cursor.fetchone():
            print(f"{name} does not exist in inventory")
            return

        self.cursor.execute(
            """DELETE FROM stock WHERE LOWER(name) = LOWER(?)""", (name,)
        )
        self.conn.commit()
        print(f"{name} removed from stock table")

    def list_teas(self):
        """Function that lists all rows in the tea inventory table (table name: stock)"""
        self.cursor.execute(
            """
                            SELECT
                                name,
                                primary_type,
                                subtype,
                                source,
                                recommended_amount_tea,
                                recommended_water_ml,
                                recommended_water_temp,
                                recommended_time_secs,
                                current_stock
                            FROM stock
                            """
        )
        teas = self.cursor.fetchall()

        if not teas:
            print("No teas in stock table")
            return

        headers = [
            "Name",
            "Primary Type",
            "Subtype",
            "Source",
            "Amount (g)",
            "Water (mL)",
            "Temp (°C)",
            "Time (s)",
            "Stock (g)",
        ]

        print(tabulate(teas, headers=headers, tablefmt="pretty"))
