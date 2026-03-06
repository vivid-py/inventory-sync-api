import sqlite3

conn = sqlite3.Connection("db.db")
cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS products(" \
"id INTEGER PRIMARY KEY AUTOINCREMENT," \
"name TEXT NOT NULL," \
"price INTEGER NOT NULL," \
"amount INTEGER NOT NULL," \
"distributor TEXT NOT NULL)")

cursor.execute("INSERT INTO products(name,price,amount,distributor) VALUES (?,?,?,?)",("Sandwich", 10, 150, "Sandwich Lab"))