import pytest
from tests.helpers import test_add_tea_helper, test_remove_tea_helper


def test_create_stock_table(inventory, conn):
    """Test that the stock table was actually created"""
    cursor = conn.cursor()
    cursor.execute("select name from sqlite_master where type='table' and name='stock';")
    assert cursor.fetchone() is not None


def test_delete_stock_table(inventory, conn):
    """Tests that the stock table was actually deleted"""
    # Step one - create temporary table using same schema as primary stock table
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                primary_type TEXT NOT NULL,
                subtype TEXT NOT NULL,
                source TEXT NOT NULL,
                recommended_amount_tea REAL NOT NULL,
                recommended_water_ml  REAL NOT NULL,
                recommended_water_temp INTEGER NOT NULL,
                recommended_time_secs INTEGER NOT NULL,
                current_stock INTEGER NOT NULL);
                   """
                   )
    # Step two - drop table and verify

    inventory.delete_stock_table()

    cursor.execute("select name from sqlite_master where type='table' and name='stock';")


def test_add_tea(inventory):
    """
    Function that tests the add_tea function. This function contains test data, see test_add_tea_helper for additional code.
    Each case uses a different name to allow the test to run.
    """

    test_data = [
        # Test valid entry
        {
            "tea": {
                "name": "Overlord_A",
                "primary_type": "Oolong",
                "subtype": "High Mountain",
                "source": "Taiwan Sourcing",
                "recommended_amount_tea": 100,
                "recommended_water_ml": 200,
                "recommended_water_temp": 95,
                "recommended_time_secs": 90,
                "current_stock": 40,
            },
            "_expected": "ok",
        },
        # Test invalid entry - missing primary type
        {
            "tea": {
                "name": "Overlord_B",
                "primary_type": None,
                "subtype": "High Mountain",
                "source": "Taiwan Sourcing",
                "recommended_amount_tea": 100,
                "recommended_water_ml": 200,
                "recommended_water_temp": 95,
                "recommended_time_secs": 90,
                "current_stock": 40,
            },
            "_expected": ValueError,
        },
        # Test invalid entry - missing recommended amount of tea
        {
            "tea": {
                "name": "Overlord_C",
                "primary_type": "Oolong",
                "subtype": "High Mountain",
                "source": "Taiwan Sourcing",
                "recommended_amount_tea": None,
                "recommended_water_ml": 200,
                "recommended_water_temp": 95,
                "recommended_time_secs": 90,
                "current_stock": 40,
            },
            "_expected": ValueError,
        },
        # Test invalid entry - invalid temperature type
        {
            "tea": {
                "name": "Overlord_D",
                "primary_type": "Oolong",
                "subtype": "High Mountain",
                "source": "Taiwan Sourcing",
                "recommended_amount_tea": 5,
                "recommended_water_ml": 200,
                "recommended_water_temp": "Hot",
                "recommended_time_secs": 90,
                "current_stock": 40,
            },
            "_expected": ValueError,
        },
    ]
    test_add_tea_helper(inventory, test_data)


def test_remove_tea(inventory, conn):

    # Step 1 - insert tea into test database
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO stock (
            name, 
            primary_type, 
            subtype, 
            source, 
            recommended_amount_tea, 
            recommended_water_ml, 
            recommended_water_temp, 
            recommended_time_secs, 
            current_stock
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) ;
            """,
        (
            "Crimson Pigeon",
            "Oolong",
            "Oriental Beauty",
            "Taiwan Sourcing",
            7,
            200,
            195,
            120,
            80,
        ),
    )
    conn.commit()

    # Step 2 - test removal
    inventory.remove_tea("Crimson Pigeon")

    cursor.execute("select count(*) from stock where name = 'Crimson Pigeon';")
    assert cursor.fetchone()[0] == 0


def test_list_teas_returns_rows(inventory, conn):
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO stock (
        name, 
        primary_type, 
        subtype, 
        source, 
        recommended_amount_tea, 
        recommended_water_ml, 
        recommended_water_temp, 
        recommended_time_secs, 
        current_stock
        ) VALUES (?,?,?,?,?,?,?,?,?)""",
        (
            "Crimson Pigeon",
            "Oolong",
            "Oriental Beauty",
            "Taiwan Sourcing",
            5.0,
            195.0,
            200,
            120,
            80)
        )
    conn.commit()

    teas = inventory.list_teas()
    assert len(teas) == 1
    assert teas[0][0] == "Crimson Pigeon" # verifying first column is name

def test_list_teas_prints_table(inventory, conn, capsys):
    cursor = conn.cursor()
    cursor.execute(
            """INSERT INTO stock(
            name,
            primary_type, 
            subtype, 
            source, 
            recommended_amount_tea, 
            recommended_water_ml, 
            recommended_water_temp, 
            recommended_time_secs, 
            current_stock
            ) VALUES (?,?,?,?,?,?,?,?,?)""",
            (
                "Crimson Pigeon",
                "Oolong",
                "Oriental Beauty",
                "Taiwan Sourcing",
                8.0,
                195.0,
                95,
                120,
                80
            )
    )
    conn.commit()
    inventory.list_teas(print_table=True)
    out = capsys.readouterr().out

    assert "Crimson Pigeon" in out
    assert "Primary Type" in out

def test_list_teas_empty_table(inventory, capsys):
    """If the table is empty, list_teas should return an empty list and print a message when print_table=True."""
    teas = inventory.list_teas()
    # Should return an empty list
    assert teas == []

    # Should print a friendly message if print_table=True
    inventory.list_teas(print_table=True)
    out = capsys.readouterr().out
    assert "No teas in stock table" in out