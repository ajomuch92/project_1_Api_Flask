from flask import redirect, url_for, render_template
from flask_socketio import SocketIO, emit
from CustomFlask import CustomFlask
import json

app = CustomFlask(__name__)
app.config['SECRET_KEY'] = '3ll@N0t3Am@!'
app.threaded = True
socketio = SocketIO(app)

users = []

@app.route('/')
def index():
  return render_template('./index.html')

@app.route('/users')
def get_users():
  return json.dumps(users)

def user_connected():
  print('Usuario conectado')

@socketio.on('on-connect')
def handler_user_connected(user):
  print(user)
  id = len(users) + 1
  nuevo_usuario = {'id': id, 'user': user['user']}
  users.append(nuevo_usuario)
  socketio.emit('user-connected', nuevo_usuario)


if __name__ == '__main__':
  socketio.run(app, debug = True)