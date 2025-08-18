import sqlite3

def database_connect(event):
    connection = sqlite3.connect(event)
    return connection

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS locations(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       address TEXT NOT NULL
                       );""")

    cursor.execute(""" CREATE TABLE IF NOT EXISTS events(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       date DATE NOT NULL,
                       local_id INTEGER NOT NULL,
                       FOREIGN KEY (local_id) REFERENCES locations(id)
                       );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS participants(
                      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      email TEXT NOT NULL,
                      event_id INTEGER NOT NULL,
                      FOREIGN KEY (event_id) REFERENCES events(id)
                       );""")

if __name__ == "__main__":
    connection = database_connect("event_2.db")
    create_tables(connection)
    connection.close()

