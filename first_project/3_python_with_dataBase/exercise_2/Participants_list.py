import sqlite3 as connector

connection = connector.connect("event_2.db")
cursor = connection.cursor()

command = """SELECT * FROM participants"""
command_1 = """SELECT name FROM participants WHERE event_id = 2 """

cursor.execute(command_1)

p_list = cursor.fetchall()
print("register type from fetchall: ", type(p_list))

for participants_list in p_list:
    print("type: ", type(participants_list), "content: ", participants_list)

cursor.close()
connection.close()
