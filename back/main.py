from flask import Flask, render_template
import test

app = Flask(__name__, template_folder="../ng-aram-app/dist/ng-aram-app", static_folder="../ng-aram-app/dist/ng-aram-app")

@app.route("/")
@app.route("/static/")
def root():
    test.main()
    return render_template('index.html')

"""
@app.errorhandler(404)
def not_found_error(error):
    return render_template('index.html')
"""

if __name__ == "__main__":
    app.run()

