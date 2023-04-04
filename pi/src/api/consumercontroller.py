from flask import Blueprint
from service import simservice

consumer_controller_api = Blueprint('consumercontroller', __name__)
service = simservice


@consumer_controller_api.route("/heaterOn")
def turn_on_heater():
    if simservice.turn_on_heater():
        return "Success"
    else:
        return "Failed"


@consumer_controller_api.route("/heaterOff")
def turn_off_heater():
    if simservice.turn_off_heater():
        return "Success"
    else:
        return "Failed"


@consumer_controller_api.route("/waterOn")
def turn_on_watering_system():
    if simservice.turn_on_watering_system():
        return "Success"
    else:
        return "Failed"


@consumer_controller_api.route("/waterOff")
def turn_off_watering_system():
    if simservice.turn_off_watering_system():
        return "Success"
    else:
        return "Failed"


@consumer_controller_api.route("/humidifierOn")
def turn_on_humidifier():
    if simservice.turn_on_humidifier():
        return "Success"
    else:
        return "Failed"


@consumer_controller_api.route("/humidifierOff")
def turn_off_humidifier():
    if simservice.turn_off_humidifier():
        return "Success"
    else:
        return "Failed"


@consumer_controller_api.route("/lightOn")
def turn_on_light():
    if simservice.turn_on_light():
        return "Success"
    else:
        return "Failed"


@consumer_controller_api.route("/lightOff")
def turn_off_light():
    if simservice.turn_off_light():
        return "Success"
    else:
        return "Failed"
