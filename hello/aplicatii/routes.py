
from flask import render_template, url_for, flash, redirect, request, abort
from hello import db
from hello.aplicatii.forms import AdminForm, SuggestionForm
from hello.models import Application, Suggestion
from flask_login import current_user, login_required



from flask import Blueprint

aplicatii = Blueprint('aplicatii', __name__)


@aplicatii.route("/suggestedapps")
def suggestedapps():

    page = request.args.get('page', 1, type=int)
    aplicatie = Suggestion.query.order_by(Suggestion.date_sugested.desc()).paginate(page=page, per_page=4)  # order by suggested date
    # aplicatie = Suggestion.query.all()
    return render_template('suggestedapps.html', aplicatie=aplicatie)


@aplicatii.route("/admin", methods=['GET', 'POST'])
@login_required
def admin():
    form = AdminForm()
    if form.validate_on_submit():
        admin_item = Application(name=form.name.data, description=form.description.data, genre=form.genre.data,
                                 image_file=form.image_file.data, install_command=form.install_command.data)
        db.session.add(admin_item)
        db.session.commit()
        flash('Your suggestion has been submitted!', 'success')
        return redirect(url_for('main.home'))
    return render_template('admin.html', title='Admin', form=form, legend='New App')


@aplicatii.route("/suggestedapps/new", methods=['GET', 'POST'])
@login_required
def new_suggestion():
    form = SuggestionForm()
    if form.validate_on_submit():
        suggestion_item = Suggestion(name=form.name.data, description=form.description.data, genre=form.genre.data,
                                     id_user=current_user.id_user)
        db.session.add(suggestion_item)
        db.session.commit()
        flash('Your suggestion has been submitted!', 'success')
        return redirect(url_for('aplicatii.suggestedapps'))
    return render_template('create_suggestion.html', title='New Suggestion',
                           form=form, legend='New Suggestion')


@aplicatii.route("/suggestedapps/<int:id_suggestion>")
def suggestion(id_suggestion):
    suggestion = Suggestion.query.get_or_404(id_suggestion)
    return render_template('suggestion.html', title=suggestion.name, suggestion=suggestion)


@aplicatii.route("/suggestedapps/<int:id_suggestion>/update", methods=['GET', 'POST'])
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
        return redirect(url_for('aplicatii.suggestedapps', id_suggestion=suggestion.id_suggestion))
    elif request.method == 'GET':
        form.name.data = suggestion.name
        form.description.data = suggestion.description
        form.install_command.data = suggestion.install_command
        form.genre.data = suggestion.genre
    return render_template('create_suggestion.html', title='Update Suggestion',
                           form=form, legend='Update Suggestion')


@aplicatii.route("/suggestedapps/<int:id_suggestion>/delete", methods=['POST'])
@login_required
def delete_suggestion(id_suggestion):
    suggestion = Suggestion.query.get_or_404(id_suggestion)
    if suggestion.id_user != current_user.id_user:
        abort(403)
    db.session.delete(suggestion)
    db.session.commit()
    flash('Your suggestion has been deleted!', 'success')
    return redirect(url_for('aplicatii.suggestedapps'))