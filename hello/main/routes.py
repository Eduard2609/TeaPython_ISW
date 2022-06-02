
from flask import render_template, request, session, flash, redirect, url_for
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

@main.route("/home/<int:id_app>")
def app(id_app):
    app = Application.query.get_or_404(id_app)
    return render_template('home.html', app=app)

@main.route("/cart")
def shoping_cart():
    if "cart" not in session:
        flash ("Your cart is empty", "info")
        return render_template('cart.html', display_cart={})
    else:
        apps = session["cart"]
        dict_of_apps = {}

        for app in apps:
            application = Application.query.get(app)
    return render_template('cart.html', display_cart=dict_of_apps)

@main.route("/add_to_cart/<int:id_app>")
def add_to_cart(id_app):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(id_app)
    flash ("Added to cart", "success")
    return redirect(url_for("main.home"))

@main.route("/download")
def download():
    for app in session["cart"]:
        application = Application.query.get(app)
        print(application.install_command)
    return render_template('download.html')