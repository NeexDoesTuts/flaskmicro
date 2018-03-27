from flask import render_template # comes with flask, it is a function
from app import app

# This function takes a template filename and a variable list of template
# arguments and returns the same template, but with all the placeholders in it replaced with actual
# values. It uses Jinja2 templating engine.

@app.route("/")
@app.route("/index")
def index():
    # mock user
    user = {"username" : "Neexiey"}

    return render_template('index.html', title='Home', user=user)

# In Flask, handlers for the application routes are written as Python functions, called
# view functions. View functions are mapped to one or more route URLs so that Flask knows
# what logic to execute when a client requests a given URL.

# A decorator modifies the function that follows it. A common pattern with decorators
# is to use them to register functions as callbacks for certain events.

# Creating mock objects is a useful technique that allows you to concentrate on one part of the
# application without having to worry about other parts of the system that don’t exist yet. I want
# to design the home page of my application, and I don’t want the fact that I don’t have a user
# system in place to distract me, so I just make up a user object so that I can keep going.