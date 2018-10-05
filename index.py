from flask import redirect, render_template, request
from flask_socketio import SocketIO, emit
from CustomFlask import CustomFlask
from Connection import Connection
import json
from ExtraFiles import  get_extra_files

app = CustomFlask(__name__)
app.config['SECRET_KEY'] = '3ll@N0t3Am@!'
socketio = SocketIO(app)
conn = Connection()
users = []

@app.route('/')
def index():
  return render_template('./index.html')

@app.route('/users')
def get_users():
  return json.dumps(users)

@app.route('/messages', methods = ['GET','POST'])
def messages_handler():
  if request.method == 'POST':
    message = request.get_json(silent=True)
    inserted = conn.insert_message(message)
    if inserted:
      socketio.emit('new-message', message)
    return str(inserted)
  elif request.method == 'GET':
    result = conn.get_messages()
    return json.dumps(result)

@socketio.on('on-connect')
def handler_user_connected(user):
  id = len(users) + 1
  nuevo_usuario = {'id': id, 'name': user['user']}
  users.append(nuevo_usuario)
  socketio.emit('user-registered',nuevo_usuario)

if __name__ == '__main__':
  socketio.run(app, extra_files = get_extra_files())