from flask import Flask
from config import configurations
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

app =  Flask(__name__)
db = SQLAlchemy(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view ='auth.login'
login_manager.session_protection = "strong"

def create_app(config_name):
    app.config.from_object(configurations[config_name])
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    db.init_app(app)
    mail.init_app(app)
    return app
