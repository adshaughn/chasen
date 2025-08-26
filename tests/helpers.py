import pytest


def test_add_tea_helper(inventory, test_data):
    """Helper for running test_add_tea

    args:
    inventory: TeaInventory object being tested
    test_data: list[dict] used in test_add_tea

    """
    for i, case in enumerate(test_data):
        tea_dict = case["tea"]
        expected = case["_expected"]

        if expected == "ok":
            inventory.add_tea(**tea_dict)

        else:
            with pytest.raises(expected):
                inventory.add_tea(**tea_dict)


def test_remove_tea_helper(inventory, test_data):
    """Helper for running test_remove_tea

    args:
    inventory: TeaInventory object being tested
    test_data: list[dict] used in test_remove_tea

    """
    for i, case in enumerate(test_data):
        tea_dict = case["tea"]
        expected = case["_expected"]

        if expected == "ok":
            inventory.remove_tea(**tea_dict)

        else:
            with pytest.raises(expected):
                inventory.remove_tea(**tea_dict)
