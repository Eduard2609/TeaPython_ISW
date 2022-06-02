
from flask import render_template, request
from hello.models import Application
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    aplicatie = Application.query.order_by(Application.genre).paginate(page=page, per_page=5) # order by app name
    return render_template('home.html', aplicatie=aplicatie)


@main.route("/about")
def about():
    return render_template('about.html')
