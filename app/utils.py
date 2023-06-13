from wtforms import StringField, SubmitField
from flask import render_template, render_template_string
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from flask_wtf.file import FileField
from wtforms import RadioField
from wtforms.validators import DataRequired


class VaxelanUtils:
    def __init__(self):
        pass


class VaxelanRoute:
    def __init__(self, url, title, template):
        self.url = url
        self.title = title
        self.template = template


class VaxelanMessage:
    def __init__(self, message=None):
        self.message = message


class VaxelanUIMessage(VaxelanMessage):
    def __init__(self, message, ui_class):
        super().__init__(message)
        self.ui_class = ui_class


class VaxelanForm(FlaskForm):
    def __init__(self, form_data):
        super().__init__(form_data)

    @classmethod
    def from_request(cls, request):
        return cls(request.form)
    
    fasta_text = TextAreaField('Enter Protein Sequence in FASTA Field')
    fasta_file = FileField('Choose File')
    radio_field = RadioField('Input Format', choices=[('option1', 'Option 1'), ('option2', 'Option 2')],
                             validators=[DataRequired()])
    

class VaxelanUI():
    
    def __init__(self):
        pass

    def generate_tag_templates(self, template_tags, app, url_for):
        tag_templates = {}
        with app.app_context():
            for tag_name, tag_attrs in template_tags.items():
                tag_templates[tag_name] = []
                for attr_name, attr_values in tag_attrs.items():
                    tag_template = "<{tag}"
                    attr_template = " {attr}='{value}'"
                    tag_template = tag_template.format(tag=tag_name)
                    
                    for attr_name, attr_value in attr_values.items():
                        if '{{' in attr_value and '}}' in attr_value:
                            # Render the Jinja2 template here
                            attr_value = render_template_string(attr_value, url_for=url_for)
                        tag_template += attr_template.format(attr=attr_name, value=attr_value)
                    tag_template += "></{tag}>\n".format(tag=tag_name)
                    tag_templates[tag_name].append(tag_template)
                tag_templates[tag_name] = "".join(tag_templates[tag_name])
        return tag_templates

