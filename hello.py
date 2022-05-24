from flask import Flask, render_template
app = Flask(__name__)

aplicatie = [
    {
        'Application_ID': '1',
        'Application_Name': 'Google Drive',
        'Install_command': 'choco install google-drive-file-stream',
    },
   {
        'Application_ID': '2',
        'Application_Name': ' Discord',
        'Install_command': 'choco install discord',
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', aplicatie=aplicatie)

@app.route("/about")
def about():
    return  render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
