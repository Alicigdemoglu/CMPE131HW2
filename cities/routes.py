from flask import render_template, url_for, flash, redirect
from cities.forms import TopCities
from cities import app

top_cities = [
    "Paris", "London", "Rome", "Tahiti"
]

title = 'top cities'

name = 'ali'


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = TopCities()
    if form.validate_on_submit():
        flash(f'Form Submitted for {form.city_name.data}!',
              category='success')
        return redirect(url_for('home'))

    return render_template("templates/home.html",
                           title=title,
                           name=name,
                           top_cities=top_cities,
                           form=form)
