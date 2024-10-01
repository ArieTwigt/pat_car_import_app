from flask import Flask, render_template, request
from utils.import_functions import import_cars_by_brand


# initiate a flask application
app = Flask(__name__)


# add the first route
@app.route('/')
def index():
    return render_template("index.html")


# add the route to import a car
@app.route("/import_car", methods=['GET', 'POST'])
def import_car():
    if request.method == 'POST':
        # car brand
        selected_brand = request.form['brand']

        # import the cars
        cars_list = import_cars_by_brand(selected_brand)
        return render_template("import_car.html",
                            cars_list = cars_list)
    else:
        return render_template("import_car.html")


# run the app
app.run()