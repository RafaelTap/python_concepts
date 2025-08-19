import sqlite3 as connector

connection = connector.connect("event_2.db")
connection.execute("PRAGMA foreign_keys = on")
cursor = connection.cursor()

command = """UPDATE events SET date  = '2025-10-22' 
             WHERE name = 'Gabys birthday'"""

cursor.execute(command)
connection.commit()

cursor.close()
connection.close()