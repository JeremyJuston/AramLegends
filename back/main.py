from flask import Flask, render_template

app = Flask(__name__, template_folder='../ng-aram-app/src/app')

@app.route("/", methods=['GET'])
def root():
    return render_template('app.component.html')
