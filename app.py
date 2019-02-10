#!/usr/bin/env python3

from flask import Flask, jsonify, request
import wordplay


app = Flask(__name__)


@app.route("/")
def hello():
    return """Flask is running!
    try the <a href="/api/v1/data">data</a> endpoint
    """


@app.route("/api/v1/data")
def dummy_data():
    data = {'message': 'looks like it works!',
            'values': list(range(9))}
    return jsonify(data)


@app.route("/api/v1/score")
def score_word():
    letters = request.args.get('w')
    score = wordplay.score_word(letters)
    result = {'letters': sorted(list(letters)),
              'score': score}
    return jsonify(result)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
