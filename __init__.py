from flask import Flask, render_template
from .db import*

app = Flask(__name__)


@app.route('/')
def index():
    database = data('inginious.sqlite')
    return render_template('index.html', noms=database[0], notes=database[1], notes2=database[2])


if __name__ == '__main__':
    app.run(debug=True)
