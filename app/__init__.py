from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on("connect")
def connect():
    print('Client connected')



@socketio.on("my_event")
def my_event(data):
    print(data)
    socketio.emit("my_response", {'data': 'Connected'})
