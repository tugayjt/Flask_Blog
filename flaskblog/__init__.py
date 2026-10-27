from flask import Flask
from .extension import db

app = Flask(__name__)
app.config['SECRET_KEY'] = '25ecffa6f1f832bb435dab4d57ed3ee9'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
db.init_app(app)

from flaskblog import routes