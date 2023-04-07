import json
import threading
import time

from flask import request

from model.responses.basicresponse import BasicResponse
from sockets.extension import socketio
from flask_socketio import emit
from service import simservice

service = simservice


def send_sensor_data():
    global emit_data
    while emit_data:
        time.sleep(1)
        response = service.get_data()
        socketio.emit('data_from_pi', json.dumps(response.__dict__))
        print("data emited")


data_thread = None
emit_data = False

users = []

@socketio.on('connect')
def handle_connect():
    global data_thread
    global emit_data
    users.append(request.sid)
    emit_data = True
    if data_thread is None:
        data_thread=threading.Thread(target=send_sensor_data)
        data_thread.start()
    print('Client connected')

@socketio.on('disconnect')
def disconnect():
    global emit_data
    global data_thread
    users.remove(request.sid)
    if not users:
        emit_data = False
        data_thread = None
    print('Client disconnected')





