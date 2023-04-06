import json
import threading
import time

from model.responses.basicresponse import BasicResponse
from sockets.extension import socketio
from flask_socketio import emit
from service import simservice

service = simservice


def update():
    time.sleep(1)
    response = service.get_data()
    json_resp = json.dumps(response.__dict__)
    emit('get_data', json_resp, broadcast=True)

@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('my event')
def handle_message(message):
    print('received message: ' + message)
    emit('my response', {'data': 'got it!'})

@socketio.on('get_data')
def handle_message(message):
    print("get data has been called")




