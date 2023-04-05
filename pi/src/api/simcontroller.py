from flask import Blueprint, Response
from service import simservice
from flask import request

sim_controller_api = Blueprint('simcontroller', __name__)
service = simservice



@sim_controller_api.route("/startAllSim")
def start_all_sim():
    """
        Starts all simulators
        ---
        responses:
            200:
                description: Ok
            400:
                description: Wrong request
         """

    service.run_all_simulator()
    return "simulator started running"

@sim_controller_api.route("/stopAllSim")
def stop_all_sim():
    service.stop_all_simulator()
    return "All simulator stopped"

@sim_controller_api.route("/setTickerSpeed")
def set_ticker_speed():
    try:
        ticker_speed = request.args.get('ticker_speed')
        if ticker_speed is None:
            return Response("Bad Request, ticker speed is missing", 400)
        else:
            float_ticker_speed = float(ticker_speed)
            service.set_ticker_speed(float_ticker_speed)
            return Response("Success, ticker speed has been set", 200)
    except:
        return Response("Something went wrong", 500)





