import os
from flask import render_template, send_from_directory
from app import app

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/gen-template')
def gen_template():
    return render_template('index.html', name="Flask")

@app.route('/profile')
def profile():
    return render_template('profile.html')

