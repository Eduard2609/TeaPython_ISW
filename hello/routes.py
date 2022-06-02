import os
import secrets
from datetime import datetime
from flask import render_template, url_for, flash, redirect, request, abort
from hello import app, db, bcrypt
from hello.forms import RegistrationForm, LoginForm, AdminForm, UpdateAccountForm, SuggestionForm
from hello.models import User, Application, Suggestion
from flask_login import login_user, current_user, logout_user, login_required


# aplicatie = [
#     {
#         'Application_ID': '1',
#         'Application_Name': 'Google Drive',
#         'Install_command': 'choco install google-drive-file-stream',
#     },
#     {
#         'Application_ID': '2',
#         'Application_Name': ' Google Chrome',
#         'Install_command': 'choco install googlechrome',
#     },
#     {
#         'Application_ID': '3',
#         'Application_Name': ' Discord',
#         'Install_command': 'choco install discord',
#     }
# ]


@app.route("/")
@app.route("/home")
def home():
    # image_file = url_for('static', filename='app_pics/default.jpg')
    # aplicatie = Application.query.all()
    page = request.args.get('page', 1, type=int)
    aplicatie = Application.query.order_by(Application.genre).paginate(page=page, per_page=5) # order by app name
    return render_template('home.html', aplicatie=aplicatie)


@app.route("/about")
def about():
    return render_template('about.html')


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


@app.route("/suggestedapps")
def suggestedapps():

    page = request.args.get('page', 1, type=int)
    aplicatie = Suggestion.query.order_by(Suggestion.date_sugested.desc()).paginate(page=page, per_page=4)  # order by suggested date 
    # aplicatie = Suggestion.query.all()
    return render_template('suggestedapps.html', aplicatie=aplicatie)


@app.route("/admin", methods=['GET', 'POST'])
@login_required
def admin():
    form = AdminForm()
    if form.validate_on_submit():
        admin_item = Application(name=form.name.data, description=form.description.data, genre=form.genre.data,
                                 image_file=form.image_file.data, install_command=form.install_command.data)
        db.session.add(admin_item)
        db.session.commit()
        flash('Your suggestion has been submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('admin.html', title='Admin', form=form, legend='New App')


@app.route("/suggestedapps/new", methods=['GET', 'POST'])
@login_required
def new_suggestion():
    form = SuggestionForm()
    if form.validate_on_submit():
        suggestion_item = Suggestion(name=form.name.data, description=form.description.data, genre=form.genre.data,
                                     id_user=current_user.id_user)
        db.session.add(suggestion_item)
        db.session.commit()
        flash('Your suggestion has been submitted!', 'success')
        return redirect(url_for('suggestedapps'))
    return render_template('create_suggestion.html', title='New Suggestion',
                           form=form, legend='New Suggestion')


@app.route("/suggestedapps/<int:id_suggestion>")
def suggestion(id_suggestion):
    suggestion = Suggestion.query.get_or_404(id_suggestion)
    return render_template('suggestion.html', title=suggestion.name, suggestion=suggestion)


@app.route("/suggestedapps/<int:id_suggestion>/update", methods=['GET', 'POST'])
@login_required
def update_sugestion(id_suggestion):
    suggestion = Suggestion.query.get_or_404(id_suggestion)
    if suggestion.id_user != current_user.id_user:
        abort(403)
    form = SuggestionForm()
    if form.validate_on_submit():
        suggestion.name = form.name.data
        suggestion.description = form.description.data
        suggestion.install_command = form.install_command.data
        suggestion.genre = form.genre.data
        db.session.commit()
        flash('Your suggestion has been updated!', 'success')
        return redirect(url_for('suggestedapps', id_suggestion=suggestion.id_suggestion))
    elif request.method == 'GET':
        form.name.data = suggestion.name
        form.description.data = suggestion.description
        form.install_command.data = suggestion.install_command
        form.genre.data = suggestion.genre
    return render_template('create_suggestion.html', title='Update Suggestion',
                           form=form, legend='Update Suggestion')


@app.route("/suggestedapps/<int:id_suggestion>/delete", methods=['POST'])
@login_required
def delete_suggestion(id_suggestion):
    suggestion = Suggestion.query.get_or_404(id_suggestion)
    if suggestion.id_user != current_user.id_user:
        abort(403)
    db.session.delete(suggestion)
    db.session.commit()
    flash('Your suggestion has been deleted!', 'success')
    return redirect(url_for('suggestedapps'))


