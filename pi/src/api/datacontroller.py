from flask import Blueprint, json, Response
from service import simservice
from model.sensordata import SensorData

data_controller_api = Blueprint('datacontroller', __name__)

service = simservice


@data_controller_api.route("/get_data")
def get_data():
    """
    Returns the sensor read data
    ---
    responses:
        200:
            description: Ok
            content:
                application/json

        400:
            description: Wrong request
    """
    try:
        result = service.get_data()
        json_str = json.dumps(result.__dict__)
        return json_str
    except:
        Response("Something wnt wrong")
