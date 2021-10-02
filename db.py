import sqlite3
DATABASE_NAME = "product.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS product(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                producType TEXT NOT NULL, 
				price INTEGER NOT NULL,
				rating INTEGER NOT NULL,
                image TEXT NOT NULL,
                description TEXT NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
