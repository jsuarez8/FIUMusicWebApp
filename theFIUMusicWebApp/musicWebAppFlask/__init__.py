from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "very_strong_and_difficult_key"

from musicWebAppFlask import routes
