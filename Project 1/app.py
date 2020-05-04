from flask import Flask, render_template

from data import tours

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', tours=tours.values())


@app.route('/departures/<departure>/')
def render_departures(departure):
    return render_template('departure.html')


@app.route('/tours/<id>/')
def render_tour(id):
    return render_template('tour.html')


app.run(debug=True)
