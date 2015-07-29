#!/usr/bin/env python
from flask import Flask, request, render_template, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/1')
def test1():
    return render_template("test1.html", saying=["He who laughs last last first.", "Alls wel that ends well"])


@app.route('/<f>')
def f(f):
    return render_template(f)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=65511,
    )
