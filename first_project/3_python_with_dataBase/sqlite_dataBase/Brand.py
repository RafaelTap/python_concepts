import sqlite3 as connector

try:
    connection = connector.connect("class.db")
    cursor = connection.cursor()
    comand = """CREATE TABLE mark(
                   id INTEGER NOT NULL,
                   name TEXT NOT NULL,
                   initialism CHARACTER(2) NOT NULL,
                   PRIMARY KEY (id)
    );"""
    cursor.execute(comand)
    connection.commit()
except connector.DatabaseError as error:
    print("error: ", error)
finally:
    cursor.close()
    connection.close()
