from app import app
from flask import render_template
import random

@app.route("/")
def home():
    elements = []
    elements.append('babo')
    elements.append('test')
    elements.append('noob')
    elements.append('hello')

    return render_template('main.html', elements=elements, index=random.randrange(1, 5))
