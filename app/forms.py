from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email, DataRequired


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Name Required")])

    email = EmailField("Email", validators=[DataRequired("Email Required"), Email("Please enter a valid e-mail address")])

    subject = StringField("Subject", validators=[DataRequired("Subject Required")])

    message = TextAreaField("Message", validators=[DataRequired("Message Required")])
