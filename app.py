# Import needed packages
from flask import Flask, render_template, request, jsonify, redirect

# Declare app instance
app = Flask(__name__)

app.data = {
    'pie': {
        'name': 'Strawberry Rhubarb Pie',
        'ingredients': [
            'strawberries',
            'rhubarb',
            'piecrust'
        ]
    }
}

# Declare app routes
@app.route('/')
def home():
    return 'Hello World'

@app.route('/greeting')
def greeting():
    return render_template('greetings.html', name='Rachel Maddow')

@app.route('/pie')
def pie():
    return jsonify({'pie ingredient': app.data['pie']['ingredients'][1]})

@app.route('/recipe', methods=('GET', 'POST'))
def recipe():
    if request.method == 'GET':
        #  Render a template that shows the name of a pie, all ingredients, and a new ingredient form
        return render_template('recipe.html', pie=app.data['pie'])
    elif request.method == 'POST':
        # The form from the GET page sends a new ingredient. Add this to your ingredients list then redirect back to `/recipe`
        # Assume we are accepting form data
        ing = str(request.form['ing'])
        app.data['pie']['ingredients'].append(ing)
        return redirect('/recipe')