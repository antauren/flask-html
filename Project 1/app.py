from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'здесь будет главная'


@app.route('/departures/<departure>/')
def render_departures(departure):
    return 'здесь будет направление'


@app.route('/tour/<id>/')
def render_tour(id):
    return 'здесь будет тур'


app.run()
