from app import app
from flask import render_template

@app.route("/")
def home():
    x = 10
    
    return render_template('main.html')
