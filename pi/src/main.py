
from flask import Flask, jsonify
from flask_swagger import swagger
from api.simcontroller import sim_controller_api
from api.datacontroller import data_controller_api
from api.consumercontroller import consumer_controller_api
from sockets.datasocket import socketio
from api.swaggerconfig import swaggerui_blueprint

from service import simservice

service = simservice

app = Flask(__name__)

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)


app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(sim_controller_api)
app.register_blueprint(data_controller_api)
app.register_blueprint(consumer_controller_api)

app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "secret"


socketio.init_app(app)


if __name__ == '__main__':
    socketio.run(app, port=5000, host='0.0.0.0')


