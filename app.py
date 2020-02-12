# Import needed packages
from flask import Flask, render_template, request

# Declare app instance
app = Flask(__name__)

# Declare app routes
@app.route('/')
def home():
    return 'Hello World'

@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Rachel Maddow')

@app.route('/pie')
def pie():
    return 'Pie JSON object?'