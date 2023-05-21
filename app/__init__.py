import json

from flask import Flask
from flask_socketio import SocketIO
import openai
from openai.error import APIConnectionError, InvalidRequestError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on("connect")
def connect():
    print('Client connected')


@socketio.on("disconnect")
def disconnect():
    print('Client disconnected')


@socketio.on("chat")
def chat_event(json_str):
    try:
        data = json.loads(json_str)
        completions = openai.ChatCompletion.create(
            messages=data,
            stream=True,
            model="gpt-3.5-turbo"
        )
        for chunk in completions:
            chunk_message = chunk['choices'][0]['delta']
            res = chunk_message.get('content', '')
            print(res, end='')
            socketio.emit("chat_response", res)
    except InvalidRequestError:
        socketio.emit("chat_response", "InvalidRequestError")
    except APIConnectionError or TimeoutError:
        socketio.emit("chat_response", "APIConnectionError")


@socketio.on("image")
def image_event(prompt):
    try:
        image_url = openai.Image.create(
            prompt=prompt,
            response_format="url",
            n=1,
            size="512x512"
        )["data"][0]["url"]
        socketio.emit("image_response", image_url)
    except InvalidRequestError:
        socketio.emit("image_response", "InvalidRequestError")
    except APIConnectionError or TimeoutError:
        socketio.emit("image_response", "APIConnectionError")


