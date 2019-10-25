from flask import Flask
from flask_login import LoginManager
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('config')

login = LoginManager(app)
login.login_view = 'login'

mysql = MySQL(app)

from demo import routes
from demo import models