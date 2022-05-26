import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from hello import app, db, bcrypt
from hello.login import RegistrationForm, LoginForm, AdminForm, SuggestionForm, UpdateAccountForm
from hello.models import User, Application, Suggestion
from flask_login import login_user, current_user, logout_user, login_required

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
    image_file = url_for('static', filename='app_pics/default.jpg')
    return render_template('home.html', aplicatie=aplicatie)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/admin")
def admin():
    form = AdminForm()
    return render_template('admin.html', title='Admin', form=form)


@app.route("/suggestion", methods=['GET', 'POST'])
@login_required
def suggestion():
    form = SuggestionForm()
    return render_template('suggestion.html', title='Suggestion', form=form)


@app.route("/suggestedapps")
def suggestedapps():
    return render_template('suggestedapps.html', aplicatie=aplicatie)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)