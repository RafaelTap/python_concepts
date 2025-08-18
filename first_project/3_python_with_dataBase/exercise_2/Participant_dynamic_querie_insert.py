from Participant import Participant
import sqlite3 as connector

try:
    connection = connector.connect("event_2.db")
    cursor = connection.cursor()

    participant_1 = Participant('rafael barros', 'rb@email.com', 1)
    participant_2 = Participant('vanuza salles', 'vs@email.com', 1)
    participant_3 = Participant('pablo marcos', 'pm@email.com', 1)
    participant_4 = Participant('marcos antonio', 'ma@email.com', 1)
    participant_5 = Participant('elaine de assis', 'ea@email.com', 1)
    participant_6 = Participant('maraiza telles', 'ml@email.com', 2)
    participant_7 = Participant('mariana vieira', 'mv@email.com', 2)
    participant_8 = Participant('talles nocete', 'tn@email.com', 2)
    participant_9 = Participant('marcos almeida', 'ma@email.com', 2)
    participant_10 = Participant('viviane cardoso', 'vc@email.com', 2)

    command = """ INSERT INTO participants (name, email, event_id) VALUES (?,?,?)"""

    cursor.execute(command, (participant_1.name, participant_1.email, participant_1.event_id))
    cursor.execute(command, (participant_2.name, participant_2.email, participant_2.event_id))
    cursor.execute(command, (participant_3.name, participant_3.email, participant_3.event_id))
    cursor.execute(command, (participant_4.name, participant_4.email, participant_4.event_id))
    cursor.execute(command, (participant_5.name, participant_5.email, participant_5.event_id))
    cursor.execute(command, (participant_6.name, participant_6.email, participant_6.event_id))
    cursor.execute(command, (participant_7.name, participant_7.email, participant_7.event_id))
    cursor.execute(command, (participant_8.name, participant_8.email, participant_8.event_id))
    cursor.execute(command, (participant_9.name, participant_9.email, participant_9.event_id))
    cursor.execute(command, (participant_10.name, participant_10.email, participant_10.event_id))

    connection.commit()

except connector.DatabaseError as error:
    print("error: ", error)

finally:
    cursor.close()
    connection.close()