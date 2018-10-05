import sqlite3
from sqlite3 import Error

class Connection():
  def __init__(self):
    pass
  
  def get_messages(self):
    connection = sqlite3.connect('./mensajes.db')
    result = connection.execute('SELECT * FROM mensajes')
    return result.fetchall()
  
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

