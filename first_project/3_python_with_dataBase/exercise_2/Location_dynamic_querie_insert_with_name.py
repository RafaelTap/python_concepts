import sqlite3 as connector
from Location import Location

connection = connector.connect("event_2.db")
cursor = connection.cursor()

location_1 = Location("warehouse", "large avenue, 1444")
location_2 = Location("rafaels house", "fire ball street, 55")

command = """INSERT INTO locations (name, address) VALUES (:name, :address)"""

cursor.execute(command, ({"name":location_2.name,
                          "address": location_2.address
                            }))

connection.commit()

cursor.close()
connection.close()