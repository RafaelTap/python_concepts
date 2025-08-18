import sqlite3 as connector

try:
    connection = connector.connect("class.db")
    cursor = connection.cursor()

    comand = """ALTER TABLE pessoa RENAME TO person;"""
    cursor.execute(comand)
    connection.commit()

except connector.DatabaseError as error:
    print("error: ", error)

finally:
    cursor.close()
    connection.close()
