from flask import (render_template,
                Blueprint,
                send_from_directory,
                request,
                redirect,
                url_for,
                session,
                current_app,
                )
from .constants import VaxelanConstants
from .utils import VaxelanForm

VaxelanBP = Blueprint('VaxelanBP', __name__)

constants = VaxelanConstants()
routes = constants.routes
ui_text = constants.ui_text
util_fns = constants.utils_fns

@VaxelanBP.get(routes.Home.url)
def home():
    form = VaxelanForm()
    return render_template(routes.Home.template,
                            constants = constants,
                            routes = routes,
                            ui_text = ui_text,
                            page_title = routes.Home.title,
                            form = form)

@VaxelanBP.get(routes.About.url)
def about():
    return render_template(routes.About.template,
                            constants = constants,
                            routes = routes,
                            ui_text = ui_text,
                            page_title = routes.About.title)


@VaxelanBP.route(routes.download.url)
def download_file(filename):
    directory = current_app.root_path + '/downloads'
    return send_from_directory(directory, filename, as_attachment=True)


