from flask import render_template, request, Blueprint
from hello.models import Application

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    applications = Application.query.order_by(Application.genre).paginate(page=page, per_page=10) # order by app name
    return render_template('home.html', applications=applications)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
