from flask import Flask
import config

class VaxelanApp():
    flask_app = Flask(__name__)
    flask_app.config.from_object(config.DevConfig)
    def __init__(self):
        pass
    def __get_app__(self):
        return self.flask_app