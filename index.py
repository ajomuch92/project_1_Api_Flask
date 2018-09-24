from flask import redirect, url_for, render_template
from flask_socketio import SocketIO, emit
from CustomFlask import CustomFlask
from flask_cors import CORS

app = CustomFlask(__name__)
app.config['SECRET_KEY'] = '3ll@N0t3Am@!'
socketio = SocketIO(app)

@app.route('/')
def index():
  return render_template('./index.html')

@socketio.on('on-connect')
def handler_user_connected(user):
  print(user)

if __name__ == '__main__':
  socketio.run(app, debug = True)