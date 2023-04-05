from datetime import datetime
import json

from flask import Blueprint, Response

from model.responses.basicresponse import BasicResponse
from service import simservice
from flask import request

sim_controller_api = Blueprint('simcontroller', __name__)
service = simservice



@sim_controller_api.route("/start_all_sim")
def start_all_sim():
    """
    Starts all simulators
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
        service.run_all_simulator()

        response.description = "Success"
        response.status_code = 200

        return Response(json.dumps(response.__dict__), 200)
    except:
        response.description = "Something went wrong"
        response.status_code = 500

        return Response(json.dumps(response.__dict__), 500)

    return "simulator started running"

@sim_controller_api.route("/stop_all_sim")
def stop_all_sim():
    """
    Stop all simulators
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
        service.stop_all_simulator()

        response.description = "Success"
        response.status_code = 200

        return Response(json.dumps(response.__dict__), 200)
    except:
        response.description = "Something went wrong"
        response.status_code = 500

        return Response(json.dumps(response.__dict__), 500)

@sim_controller_api.route("/set_ticker_speed")
def set_ticker_speed():
    """
    Sets the simulators internal clock speed
    ---
    parameters:
        -   in: query
            name: ticker_speed
            schema:
                type: numeric
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
        ticker_speed = request.args.get('ticker_speed')
        if ticker_speed is None or ticker_speed == "":

            response.description = "Bad Request, ticker speed is missing"
            response.status_code = 400

            return Response(json.dumps(response.__dict__), 400)
        else:
            float_ticker_speed = float(ticker_speed)
            service.set_ticker_speed(float_ticker_speed)

            response.description = "Success, ticker speed has been set"
            response.status_code = 200

            return Response(json.dumps(response.__dict__), 200)
    except:
        response.description = "Something went wrong"
        response.status_code = 500

        return Response(json.dumps(response.__dict__), 500)

@sim_controller_api.route("/set_simulator_date")
def set_simulator_date():
    """
    Sets the simulators internal date
    ---
    parameters:
        -   in: query
            name: date
            schema:
                type: string
                example: '2017-07-21 17:32:28'
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

        str_sim_date = request.args.get("date")
        if str_sim_date is None or str_sim_date == "":

            response.description = "Bad Request, ticker speed is missing"
            response.status_code = 400

            return Response(json.dumps(response.__dict__), 400)
        else:
            sim_date = datetime.strptime(str_sim_date, "%Y-%m-%d %H:%M:%S")
            service.set_sim_date(sim_date)

            response.description = "Success, ticker speed has been set"
            response.status_code = 200

            return Response(json.dumps(response.__dict__), 200)
    except:
        response.description = "Something went wrong"
        response.status_code = 500

        return Response(json.dumps(response.__dict__), 500)

@sim_controller_api.route("/resume_ticker")
def resume_ticker():
    """
    Resumes the simulator internal ticker/clock
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
        service.resume_ticker()
        response.description = "Success, ticker has been resumed"
        response.status_code = 200

        return Response(json.dumps(response.__dict__), 200)
    except:
        response.description = "Something went wrong"
        response.status_code = 500

        return Response(json.dumps(response.__dict__), 500)

@sim_controller_api.route("/stop_ticker")
def stop_ticker():
    """
    Stops the simulator internal ticker/clock
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
        service.stop_ticker()
        response.description = "Success, ticker has been resumed"
        response.status_code = 200

        return Response(json.dumps(response.__dict__), 200)
    except:
        response.description = "Something went wrong"
        response.status_code = 500

        return Response(json.dumps(response.__dict__), 500)
