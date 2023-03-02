from flask import Flask, render_template
from back import champions

#app = Flask(__name__, template_folder="../ng-aram-app/src", static_folder="../ng-aram-app/dist/ng-aram-app")
app = Flask(__name__, template_folder="static/", static_folder="static/", static_url_path="")

@app.route("/")
def root():
    dataa = champions.main()
    print(dataa)
    return render_template('index.html')


@app.errorhandler(404)
def not_found_error(error):
    dataa = champions.main()
    return render_template('index.html')

@app.route("/loading/<id>")
def get_data(id):
    data = champions.get_champions_list2(id)
    #data = ["Irelia", "Jayce", "Zed perso broken", "Garen fine"]
    return data


if __name__ == "__main__":
    app.run()

