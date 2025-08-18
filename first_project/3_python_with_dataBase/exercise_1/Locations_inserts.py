import sqlite3 as connector

try:
    connection = connector.connect("event.db")
    cursor =  connection.cursor()

    command = """INSERT INTO locations(name, address)
                   VALUES ('central office', 'fire dragons street, 222 - dungeons of fire'),
                          ('Braians house','wheels of illusions, 333 - caves in fire')"""

    cursor.execute(command)
    connection.commit()

except connector.DatabaseError as error:
    print("error: ", error)

finally:
    cursor.close()
    connection.close()
