import sqlite3 as connector

try:
    connection = connector.connect("event.db")
    cursor = connection.cursor()

    command = """INSERT INTO participants (name, email, event_id)
                 VALUES ('rafael barros', 'rb@email.com', 1),
                 ('vanuza salles', 'vs@email.com', 1),
                 ('pablo marcos', 'pm@email.com', 1),
                 ('marcos antonio', 'ma@email.com', 1),
                 ('elaine de assis', 'ea@email.com', 1),
                 ('maraiza telles', 'ml@email.com', 2),
                 ('mariana vieira', 'mv@email.com', 2),
                 ('talles nocete', 'tn@email.com', 2),
                 ('marcos almeida', 'ma@email.com', 2),
                 ('viviane cardoso', 'vc@email.com', 2);"""

    cursor.execute(command)
    connection.commit()

except connector.DatabaseError as error:
    print("error: ", error)

finally:
    cursor.close()
    connection.close()

