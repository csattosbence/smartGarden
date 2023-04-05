import json

from flask import Blueprint, Response

from model.responses.basicresponse import BasicResponse
from service import simservice

consumer_controller_api = Blueprint('consumercontroller', __name__)
service = simservice



@consumer_controller_api.route("/heater_on")
def turn_on_heater():
    """
    Turns on the heater
    ---
    responses:
        200:
            description: Ok
            content:
                application/json

        400:
            description: Wrong request
    """
    response = BasicResponse()
    try:
        simservice.turn_on_heater()

        response.status_code = 200
        response.description = "Heater has been successfully turned on"

        return Response(json.dumps(response.__dict__),200)
    except:
        response.status_code = 500
        response.description = "Something went wrong"

        return Response(json.dumps(response.__dict__), 500)


@consumer_controller_api.route("/heater_off")
def turn_off_heater():
    """
    Turns off the heater
    ---
    responses:
        200:
            description: Ok
            content:
                application/json

        400:
            description: Wrong request
    """
    response = BasicResponse()
    try:
        simservice.turn_off_heater()

        response.status_code = 200
        response.description = "Heater has been successfully turned off"

        return Response(json.dumps(response.__dict__), 200)
    except:
        response.status_code = 500
        response.description = "Something went wrong"

        return Response(json.dumps(response.__dict__), 500)


@consumer_controller_api.route("/water_on")
def turn_on_watering_system():
    """
    Turns on the watering system
    ---
    responses:
        200:
            description: Ok
            content:
                application/json

        400:
            description: Wrong request
    """
    response = BasicResponse()
    try:
        simservice.turn_on_watering_system()

        response.status_code = 200
        response.description = "Watering system has been successfully turned on"

        return Response(json.dumps(response.__dict__), 200)
    except:
        response.status_code = 500
        response.description = "Something went wrong"

        return Response(json.dumps(response.__dict__), 500)

@consumer_controller_api.route("/water_off")
def turn_off_watering_system():
    """
    Turns on the watering system
    ---
    responses:
        200:
            description: Ok
            content:
                application/json

        400:
            description: Wrong request
    """
    response = BasicResponse()
    try:
        simservice.turn_off_watering_system()

        response.status_code = 200
        response.description = "Watering system has been successfully turned off"

        return Response(json.dumps(response.__dict__), 200)
    except:
        response.status_code = 500
        response.description = "Something went wrong"

        return Response(json.dumps(response.__dict__), 500)


@consumer_controller_api.route("/humidifier_on")
def turn_on_humidifier():
    """
    Turns on the humidifier
    ---
    responses:
        200:
            description: Ok
            content:
                application/json

        400:
            description: Wrong request
    """
    response = BasicResponse()
    try:
        simservice.turn_on_humidifier()

        response.status_code = 200
        response.description = "Humidifier has been successfully turned on"

        return Response(json.dumps(response.__dict__), 200)
    except:
        response.status_code = 500
        response.description = "Something went wrong"

        return Response(json.dumps(response.__dict__), 500)


@consumer_controller_api.route("/humidifier_off")
def turn_off_humidifier():
    """
    Turns off the humidifier
    ---
    responses:
        200:
            description: Ok
            content:
                application/json

        400:
            description: Wrong request
    """
    response = BasicResponse()
    try:
        simservice.turn_off_humidifier()

        response.status_code = 200
        response.description = "Humidifier has been successfully turned off"

        return Response(json.dumps(response.__dict__), 200)
    except:
        response.status_code = 500
        response.description = "Something went wrong"

        return Response(json.dumps(response.__dict__), 500)


@consumer_controller_api.route("/light_on")
def turn_on_light():
    """
    Turns on the light system
    ---
    responses:
        200:
            description: Ok
            content:
                application/json

        400:
            description: Wrong request
    """
    response = BasicResponse()
    try:
        simservice.turn_on_light()

        response.status_code = 200
        response.description = "Light system has been successfully turned on"

        return Response(json.dumps(response.__dict__), 200)
    except:
        response.status_code = 500
        response.description = "Something went wrong"

        return Response(json.dumps(response.__dict__), 500)


@consumer_controller_api.route("/light_off")
def turn_off_light():
    """
    Turns off the light system
    ---
    responses:
        200:
            description: Ok
            content:
                application/json

        400:
            description: Wrong request
    """
    response = BasicResponse()
    try:
        simservice.turn_off_light()

        response.status_code = 200
        response.description = "Light system has been successfully turned off"

        return Response(json.dumps(response.__dict__), 200)
    except:
        response.status_code = 500
        response.description = "Something went wrong"

        return Response(json.dumps(response.__dict__), 500)
