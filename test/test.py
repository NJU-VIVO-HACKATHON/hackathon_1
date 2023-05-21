import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('Connected to the server')
    # 发送事件
    sio.emit('my_event', {'data': 'Connected'})


@sio.event
def disconnect():
    print('Disconnected from the server')


@sio.on('my_response')
def my_response_handler(data):
    print('Received: ', data)


sio.connect('http://localhost:5000')
