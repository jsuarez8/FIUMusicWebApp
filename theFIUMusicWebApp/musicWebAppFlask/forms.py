from musicWebAppFlask import app
from wtforms import SelectField, StringField, SubmitField
from flask_wtf import FlaskForm


class MusicForms(FlaskForm):
    chart = SelectField("chart", choices=[
        ("top", "Top tracks by editorial chart"),
        ("hot", "Most viewed lyrics in the last 2 hours"),
        ("mxmweekly", "Most viewed lyrics in the last 7 days"),
        ("mxmweekly_new", "Most viewed new-released lyrics in the last 7 days"),
    ])
    country = StringField("Country")
    submit = SubmitField("Submit")
