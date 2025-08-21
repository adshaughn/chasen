from chasen_app import ChasenApp
import sqlite3
import os


def main():
    app = ChasenApp(conn)
    app.run()


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/chasen.db")
    main(conn)
