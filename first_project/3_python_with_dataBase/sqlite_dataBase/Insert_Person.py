import sqlite3 as connector

try:
    connection = connector.connect("class.db")
    cursor = connection.cursor()

    comand = """INSERT INTO person (cpf, name, birthday, glasses)
                    VALUES (12345675647, 'rafael lares', '2000-02-12', true),
                        (34539586754, 'vitor matheus', '1999-05-20', true),
                        (48567374632, 'luis guimaraes', '1994-12-21', false),
                        (20367541983, 'larissa ventura', '1990-10-11', false),
                        (33994857632, 'manuela tavares', '1992-02-20', true)
    """
    cursor.execute(comand)
    connection.commit()
except connector.DatabaseError as error:
    print("error: ", error)
except Exception as e:
   print("error: ", e)
finally:
    cursor.close()
    connection.close()