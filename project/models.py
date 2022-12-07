from datetime import datetime
from project import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    sugestion = db.relationship('Suggestion', backref='user', lazy=True)
    role = db.Column(db.String(20), nullable=True, default='user', )

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def get_id(self):
        return self.id_user


class Application(db.Model):
    id_application = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    install_command = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Application('{self.name}', '{self.description}', '{self.genre}', " \
               f"'{self.install_command}', '{self.image_file}') "


class Suggestion(db.Model):
    id_suggestion = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    genre = db.Column(db.String(20), unique=True, nullable=False)
    install_command = db.Column(db.String(120), nullable=True)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    date_sugested = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)

    def get_user(self):
        return User.query.get(int(self.id_user))

    def __repr__(self):
        return f"Suggestion('{self.name}', '{self.description}', '{self.genre}', " \
               f"'{self.image_file}', '{self.date_sugested}')"
               
def init_db():
    db.create_all()

