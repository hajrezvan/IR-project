# Flask project
from flask import Flask, render_template, request

import QP

app = Flask(__name__)


def query(inp):
    return QP.enter(inp)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = query(request.form['query'])
        return render_template("index.html", data=data)
    else:
        return render_template("index.html")
