from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>')
def number(n):
    if isinstance(n, int):
        return '{} is a number'.format(n)
    else:
        return 'Invalid input'

@app.route('/number_template/<int:n>')
def number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', number=n)
    else:
        return 'Invalid input'
    
@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    if isinstance(n, int):
        if n % 2 == 0:
            return render_template('6-number_odd_or_even.html', number=n, odd_even='even')
        else:
            return render_template('6-number_odd_or_even.html', number=n, odd_even='odd')
    else:
        return 'Invalid input'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""Module of a python script"""

from flask import *

app = Flask(__name__)

@app.route('/',strict_slashes=False)
def home():
    """func to be executed"""
    return "Hello HBNB!"

@app.route('/hbnb',strict_slashes=False)
def hbnb():
    """func to be executed"""
    return "HBNB"

@app.route('/c/<text>',strict_slashes=False)
def cisvariable(text):
    """func to be executed"""
    text=text.replace("_", " ")
    return f"C {text}"

@app.route('/python/<text>',strict_slashes=False)
def pythonisvariable(text = "is cool"):
    """func to be executed"""
    if text:
        text=text.replace("_", " ")
        return f"Python {text}"
    return f"Python {text}"


@app.route('/number/<int:n>',strict_slashes=False)
def number(n):
    """func to be executed"""

    return f"{n} is a number"


@app.route('/number_template/<int:n>',strict_slashes=False)
def number(n):
    """func to be executed"""

    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>',strict_slashes=False)
def number(n):
    """func to be executed"""

    return render_template("6-number_odd_or_even.html", n=n)

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=5000)
