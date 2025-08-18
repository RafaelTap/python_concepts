from Event import Event
import sqlite3 as connector

try:
    connection = connector.connect("event_2.db")
    cursor = connection.cursor()

    event_1 = Event('Gabys birthday', '2025-10-17', 1)
    event_2 = Event('HSBC Arena', '2025-08-22', 2)

    comand = """ INSERT INTO events (name, date, local_id) VALUES (?,?,?);"""

    cursor.execute(comand, (event_1.name, event_1.date, event_1.local_id))
    cursor.execute(comand, (event_2.name, event_2.date, event_2.local_id))

    connection.commit()

except connector.DatabaseError as error:
    print("error: ", error)

finally:
    cursor.close()
    connection.close()
