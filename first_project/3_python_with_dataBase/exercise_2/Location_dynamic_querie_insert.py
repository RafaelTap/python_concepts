from Location import Location
import sqlite3 as connector

try:
    connection = connector.connect("event_2.db")
    cursor = connection.cursor()

    location_1 = Location('Party House', 'main street, 22')
    location_2 = Location('HSBC Arena', 'joshua hernandez street, 69')

    comand = """ INSERT INTO locations (name, address) VALUES (?,?);"""

    cursor.execute(comand, (location_1.name, location_1.address))
    cursor.execute(comand, (location_2.name, location_2.address))

    connection.commit()

except connector.DatabaseError as error:
    print("error: ", error)

finally:
    cursor.close()
    connection.close()

