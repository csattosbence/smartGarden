from flask import Blueprint
from service import simservice

data_controller_api = Blueprint('datacontroller', __name__)

service = simservice


@data_controller_api.route("/getTemp")
def get_temp():
    return service.get_temp()