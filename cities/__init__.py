import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "somethingrandom1234"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from cities import routes, models
