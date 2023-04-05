import threading

from flask import Flask, jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from api.simcontroller import sim_controller_api
from api.datacontroller import data_controller_api
from api.consumercontroller import consumer_controller_api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(sim_controller_api)
    app.register_blueprint(data_controller_api)
    app.register_blueprint(consumer_controller_api)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = '/spec'  # Our API url (can of course be a local resource)

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Smart Garden Simulator"
        }
    )

    app.register_blueprint(swaggerui_blueprint)

    return app

