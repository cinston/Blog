from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads

bootstrap = Bootstrap()
db = SQLAlchemy
mail = Mail

def create_app(config_name):
    app = Flask(__name__)
