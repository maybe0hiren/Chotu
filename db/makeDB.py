import sqlite3

connection = sqlite3.connect("chotu.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        message TEXT NOT NULL,
        deadlineDate TEXT,
        deadlineDay TEXT,
        deadlineTime TEXT,
        type TEXT NOT NULL,
        recurring BOOLEAN NOT NULL DEFAULT 0,

        CHECK (
            deadlineDate IS NOT NULL
            OR deadlineDay IS NOT NULL
        )
    )
""")

connection.commit()
connection.close()

print("Tasks table created successfully.")