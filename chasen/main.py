import os
import sqlite3

from chasen_app import ChasenApp


def main():
    app = ChasenApp(conn)
    app.run()


if __name__ == "__main__":
    os.makedirs("../data", exist_ok=True)
    conn = sqlite3.connect("../data/chasen.db")
    main(conn)
