import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('Connected to the server')
    # 发送事件
    sio.emit('image', "一张和猫有关的图片")


@sio.event
def disconnect():
    print('Disconnected from the server')


@sio.on("chat_response")
def chat_response_handle(data):
    print(data, end='')
    # print('chat_response: ', "client start chat")


@sio.on("image_response")
def image_response_handle(data):
    print(data, end='')


sio.connect('http://localhost:5000')
