#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/data")
def dummy_data():
    data = {'message': 'looks like it works!',
            'values': list(range(9))}
    return jsonify(data)
