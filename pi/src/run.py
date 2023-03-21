import threading

from flask import Flask
from api.simcontroller import sim_controller_api
from api.datacontroller import data_controller_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(sim_controller_api)
    app.register_blueprint(data_controller_api)
    return app

