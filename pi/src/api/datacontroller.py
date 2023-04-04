from flask import Blueprint, json
from service import simservice
from model.sensordata import SensorData

data_controller_api = Blueprint('datacontroller', __name__)

service = simservice


@data_controller_api.route("/getData")
def get_data():
    result = service.get_data()
    json_str = json.dumps(result.__dict__)
    return json_str
