from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from functools import wraps
app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)



        

from app import views,models