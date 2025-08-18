import psycopg2 as connector

# creating connection with postgreSQL
connection = connector.connect(" ")

cursor = connection.cursor()

cursor.execute(" ") # sql query
cursor.fetchall()

connection.commit()

cursor.close()
connection.close()