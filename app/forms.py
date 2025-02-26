from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import InputRequired


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired("Name Required")])

    email = EmailField("Email", validators=[InputRequired("Email Required")])

    subject = StringField("Subject", validators=[InputRequired("Subject Required")])

    message = TextAreaField("Message", validators=[InputRequired("Message Required")])
