from app import app
from flask import render_template
import random
import item

from .stats import *



@app.route('/')
def home():
    return render_template('main.html')
