import random
from flask import Flask

app = Flask(__name__)


def test_print():
    return """<img src='static/images/%d.png' width='300' height='300'>""" % (random.randrange(1,8))

@app.route("/")
def home():
    return test_print()

if __name__ == '__main__':
    app.run() 