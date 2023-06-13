from .utils import VaxelanUI, VaxelanUtils
from .template_constants import template_tags, template_script_tags
from flask_app import VaxelanApp
from .route_objs import Routes
from .ui_text import UIText
from flask import url_for

class VaxelanConstants():

    navbar_routes = ['About']

    routes = Routes()

    ui_text = UIText()

    utils_fns = VaxelanUtils()

    def __init__(self):
        pass
    template_tags = template_tags
    template_script_tags = template_script_tags

    ui_setter = VaxelanUI()

    app = VaxelanApp()
    flask_app = app.__get_app__()

    tags_template = ui_setter.generate_tag_templates(template_tags, flask_app, url_for)
    tags_html = "".join(tags_template.values())
    tags_script_template = ui_setter.generate_tag_templates(template_script_tags, flask_app, url_for)
    tags_script_html = "".join(tags_script_template.values())
