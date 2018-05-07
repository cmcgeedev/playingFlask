from flask import Flask
from flask_restful import Api
from playingFlask.src.api.common import AppConfig
from playingFlask.src.api.controllers import UserController, PetController, ShelterController

app = Flask(__name__)
api = Api(app)


def bootstrap():
    load_config()
    cfg = AppConfig.get_config()
    init_logging(cfg)
    return


def load_config():
    AppConfig.load_config("appConfig.json")
    return


def init_logging(cfg):
    return


def serve_api():
    cfg = AppConfig.get_config()
    #just for testing - will remove
    api.add_resource(UserController.HelloWorld, '/v1/hello')
    api.add_resource(UserController.UserController, '/v1/user/<string:user_id>')
    api.add_resource(PetController.PetController, '/v1/pets/<string:pet_id>')
    api.add_resource(ShelterController.ShelterController,'/v1/shelters/<string:shelter_id>')
    app.run(host="0.0.0.0", port=cfg.Port, debug=cfg.Debug)
    return


if __name__ == '__main__':
    bootstrap()
    serve_api()