from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h2>Home page for the moment!</h2>"

@app.route("/about")
def about():
    return "<h2>About page for the moment!</h2>"


if __name__ == '__main__':
    app.run(debug=True)
