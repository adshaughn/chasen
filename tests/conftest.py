import sqlite3
import pytest
from chasen.inventory import TeaInventory


@pytest.fixture
def conn():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()


@pytest.fixture
def inventory(conn):
    # Assume TeaInventory.__init__(conn) creates the stock table if missing
    return TeaInventory(conn)
