from flask import Flask, request
from pi import find_pi

app = Flask(__name__)


@app.route("/")
def index():
    return "fff"


@app.route("/calc")
def calc():
    a = int(request.args.get("a", 22))
    result = find_pi(a)
    return str(result)
