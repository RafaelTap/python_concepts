import sqlite3 as connector
from Participant import Participant

connection = connector.connect("event_2.db")
cursor = connection.cursor()

command = """SELECT * FROM participants"""

