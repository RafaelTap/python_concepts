import sqlite3 as connector

connection = connector.connect("event.db")
cursor = connection.cursor()

command = """SELECT * FROM participants"""
command_2 = "SELECT name, email FROM participants WHERE event_id = 1"

cursor.execute(command_2)

p_list = cursor.fetchall()

for part_list in p_list:
    print("-->", part_list)

cursor.close()
connection.close()