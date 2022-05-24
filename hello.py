from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
