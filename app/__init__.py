from .views import VaxelanBP
from flask_app import VaxelanApp

class VaxelanInit():
    flask_app = VaxelanApp().__get_app__()
    flask_app.static_url_path = flask_app.config.get("STATIC_FOLDER")
    flask_app.static_folder = flask_app.config.get("STATIC_FOLDER")
    flask_app.template_folder = flask_app.config.get("TEMPLATES_FOLDER")
    flask_app.secret_key = flask_app.config.get("SECRET_KEY")
    flask_app.instance_path = flask_app.config.get("INSTANCE_PATH")
    flask_app.register_blueprint(VaxelanBP)
    def __get_flask__(self):
        return self.flask_app
        