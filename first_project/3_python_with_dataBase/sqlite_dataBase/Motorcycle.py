import sqlite3 as connector

try:
    connection = connector.connect("class.db")
    cursor = connection.cursor()
    comand = """CREATE TABLE motorcycle(
                   register CHARACTER(7) NOT NULL,
                   year INTEGER NOT NULL,
                   owner INTEGER NOT NULL,
                   mark INTEGER NOT NULL,
                   PRIMARY KEY (register),
                   FOREIGN KEY (owner) REFERENCES pessoa(cpf),
                   FOREIGN KEY (MARK) REFERENCES marca(id)
    );"""
    cursor.execute(comand)
    connection.commit()

except connector.DatabaseError as error:
    print("error", error)

finally:
    cursor.close()
    connection.close()


