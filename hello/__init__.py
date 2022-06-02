from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from hello.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'  # daca nu esti logat esti redirectionat la pagina de login
login_manager.login_message_category = 'warning'  # mesajul de eroare


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from hello.users.routes import users  # importam toate rutele din users cu ajutorul Blueprint
    from hello.aplicatii.routes import aplicatii
    from hello.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(aplicatii)
    app.register_blueprint(main)

    return app
