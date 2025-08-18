import sqlite3 as connector

try:
    connection = connector.connect("class.db")
    cursor = connection.cursor()

    comand = '''CREATE TABLE pessoa(
                   cpf INTEGER NOT NULL,
                   name TEXT NOT NULL,
                   birthday DATE NOT NULL,
                   glasses BOOLEAN NOT NULL,
                   PRIMARY KEY (cpf)
                   );'''

    cursor.execute(comand)
    connection.commit()
except connector.DatabaseError as error:
    print("error: ",error)

finally:
    if connection:
        cursor.close()
        connection.close()

