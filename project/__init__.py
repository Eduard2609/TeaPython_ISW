from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from project.config import Config

def create_tables():
    db.create_all()

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'  # daca nu esti logat esti redirectionat la pagina de login
login_manager.login_message_category = 'warning'  # mesajul de eroare


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from project.users.routes import users  # importam toate rutele din users cu ajutorul Blueprint
    from project.applications.routes import applications
    from project.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(applications)
    app.register_blueprint(main)

    return app
