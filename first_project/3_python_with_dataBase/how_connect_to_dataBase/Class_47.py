import mysql.connector as connector

# creating connection with mysql
connection = connector.connect(" ")

cursor = connection.cursor()

cursor.execute(" ") #sql query
cursor.fetchall()

connection.commit()

cursor.close()
connection.close()