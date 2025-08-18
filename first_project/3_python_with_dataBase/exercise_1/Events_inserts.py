import sqlite3 as connector

try:
    connection = connector.connect("event.db")
    cursor = connection.cursor()

    comand = """INSERT INTO events (name, date, local_id)
                VALUES ('development meet', '2025-08-18', 1),
                ('braians birthday', '2025-09-20', 2);"""

    cursor.execute(comand)
    connection.commit()


except connector.DatabaseError as error:
    print("Error: ", error)

except Exception as e:
    print("Error: ", e)

finally:
    cursor.close()
    connection.close()