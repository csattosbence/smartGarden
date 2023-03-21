from flask import Blueprint
from service import simservice

sim_controller_api = Blueprint('simcontroller', __name__)
service = simservice


@sim_controller_api.route("/startSim")
def start_sim():
    service.run_simulator()
    return "simulator started running"

