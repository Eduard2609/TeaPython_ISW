from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from login import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TeaBase.db'
db = SQLAlchemy(app)

# ---------------- Database model ORM ---------------- #

class Users(db.Model):
    Users_id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(30), unique=True, nullable=False)
    Password = db.Column(db.String(225), nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.Username}', '{self.Email}')"

class Applications(db.Model):
    Applications_id = db.Column(db.Integer, primary_key=True)
    Application_name = db.Column(db.String(120), unique=True, nullable=False)
    Install_command = db.Column(db.String(225), nullable=False)
    Image_file = db.Column(db.String(225), nullable=False, default='default.png')

    def __repr__(self):
        return f"Application('{self.Application_name}', '{self.Install_command}', '{self.Image_file}')"

class Genres(db.Model):
    Genres_id = db.Column(db.Integer, primary_key=True)
    Genres_name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"Genre('{self.Genre_name}')"


    def __repr__(self):
        return f"AppsGenres('{self.Application_id}', '{self.Genre_id}')"

class Presets(db.Model):
    Presets_id = db.Column(db.Integer, primary_key=True)
    Preset_name = db.Column(db.String(120), unique=True, nullable=False)
    Users_id = db.Column(db.Integer, db.ForeignKey('Users.Users_id'), nullable=False)

    def __repr__(self):
        return f"Preset('{self.Preset_name}', '{self.Users_id}')"

class AppsPresets(db.Model):
    AppsPresets_id = db.Column(db.Integer, primary_key=True)
    Presets_id = db.Column(db.Integer, db.ForeignKey('Presets.Presets_id'), nullable=False)
    Application_id = db.Column(db.Integer, db.ForeignKey('Applications.Applications_id'), nullable=False)

    def __repr__(self):
        return f"AppsPresets('{self.Presets_id}', '{self.Application_id}')"

class AppsGenres(db.Model):
    Appsgenres_id = db.Column(db.Integer, primary_key=True)
    Application_id = db.Column(db.Integer, db.ForeignKey('Applications.Applications_id'), nullable=False)
    Genres_id = db.Column(db.Integer, db.ForeignKey('Genres.Genres_id'), nullable=False)


# ---------------- Database model ORM -----END ---------------- #

# ---------------- Routes and others -------------------------- #

aplicatie = [
    {
        'Application_ID': '1',
        'Application_Name': 'Google Drive',
        'Install_command': 'choco install google-drive-file-stream',
    },
   {
        'Application_ID': '2',
        'Application_Name': ' Google Chrome',
        'Install_command': 'choco install googlechrome',
    },
    {
        'Application_ID': '3',
        'Application_Name': ' Opera ',
        'Install_command': 'choco install opera',
    },
    {
        'Application_ID': '4',
        'Application_Name': ' Opera Gx',
        'Install_command': 'choco install opera-gx',
    },
    {
        'Application_ID': '5',
        'Application_Name': ' Firefox',
        'Install_command': 'choco install firefox',
    },
    {
        'Application_ID': '6',
        'Application_Name': ' Edge',
        'Install_command': 'choco install microsoft-edge',
    },
    {
        'Application_ID': '7',
        'Application_Name': ' Discord',
        'Install_command': 'choco install discord',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', aplicatie=aplicatie)

@app.route("/about")
def about():
    return  render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'alexandru.momoi@student.unitbv.ro' and form.password.data == 'parola':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
