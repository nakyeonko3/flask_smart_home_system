import sqlite3

conn = sqlite3.connect("database.db")
print("create & connect database")

conn.execute(
    """
create table users (email text, name text)
"""
)
print("create table")

conn.close()
