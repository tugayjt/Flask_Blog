from flask import Flask
from .extension import db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '25ecffa6f1f832bb435dab4d57ed3ee9'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"
from flaskblog import routes    