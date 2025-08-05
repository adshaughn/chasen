import unittest
import sqlite3
from inventory import TeaInventory


class TestTeaInventory(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.inventory = TeaInventory(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_create_stock_table(self):
        # Test that the stock table was actually created
        cursor = self.conn.cursor()
        cursor.execute(
            "select name from sqlite_master where type='table' and name='stock';"
        )
        table = cursor.fetchone()
        self.assertIsNotNone(table)

    def test_add_tea(self):
        # First test valid case
        self.inventory.add_tea(
            "Overlord", "Oolong", "High Mountain", "Taiwan Sourcing", 5, 200, 90, 120
        )
        teas = self.inventory.list_teas()
        expected_row = ("Overlord", "Oolong", 5, 200, 90, 120)
        self.assertIn(expected_row, teas)

    # def test_list_teas(self):
    #     self.assertEqual(True, False)  # add assertion here


if __name__ == "__main__":
    unittest.main()
