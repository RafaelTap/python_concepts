import sqlite3 as connector

#creating connection with sqlite3

connection = connector.connect("")

cursor = connection.cursor()

cursor.execute("") # sql query
cursor.fetchall()

connection.commit()

cursor.close()
connection.close()