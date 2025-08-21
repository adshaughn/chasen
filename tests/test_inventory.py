import pytest
from tests.helpers import test_add_tea_helper


def test_create_stock_table(inventory, conn):
    """Test that the stock table was actually created"""
    cursor = conn.cursor()
    cursor.execute(
        "select name from sqlite_master where type='table' and name='stock';"
    )
    assert cursor.fetchone() is not None


# def test_delete_stock_table(self):
#     cursor = self.conn.cursor()
#     cursor.execute()

# below is deprecated
# def test_add_tea(inventory):
#     # First test valid case
#     inventory.add_tea(
#         "Overlord", "Oolong", "High Mountain", "Taiwan Sourcing", 5, 200, 90, 120
#     )
#     teas = self.inventory.list_teas()
#     expected_row = ("Overlord", "Oolong", "High Mountain", "Taiwan Sourcing", 5, 200, 90, 120)
#     self.assertIn(expected_row, teas)


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


# def test_list_teas(self):
#     self.assertEqual(True, False)  # add assertion here


# def test_remove_tea(self):
#     self.inventory.remove_tea(
#
#     )

# def test_list_teas(self):
#     teas = self.inventory.list_teas()
