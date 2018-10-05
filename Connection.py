import sqlite3
from sqlite3 import Error

class Connection():
  def __init__(self):
    pass
  
  def get_messages(self):
    connection = sqlite3.connect('./mensajes.db')
    result = connection.execute('SELECT * FROM mensajes')
    rows = result.fetchall()
    records = []
    for row in rows:
      record = {
        'id': row[0],
        'user': row[1],
        'text': row[2],
        'date': row[3]
      }
      records.append(record)
    return records
  
  def insert_message(self, message):
    try:
      connection = sqlite3.connect('./mensajes.db')
      query = 'INSERT INTO mensajes(usuario, mensaje, fecha) VALUES (?, ?, ?)'
      cursor = connection.cursor()
      cursor.execute(query, (message['user'], message['text'], message['date']))
      connection.commit()
      return True
    except Error as e:
      print(e)
      return False

