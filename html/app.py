# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """<h1>Helloooo</h1>
              <img src='static/images/test.png'/>"""

if __name__ == '__main__':
    app.run() 