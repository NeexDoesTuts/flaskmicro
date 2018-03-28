from flask import render_template, flash, redirect, url_for # comes with flask, it is a function
from app import app
from app.forms import LoginForm

# This function takes a template filename and a variable list of template
# arguments and returns the same template, but with all the placeholders in it replaced with actual
# values. It uses Jinja2 templating engine.

@app.route("/")
@app.route("/index")
def index():
    # mock user
    user = {"username" : "Neexiey"}

    # mock posts object
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
# In Flask, handlers for the application routes are written as Python functions, called
# view functions. View functions are mapped to one or more route URLs so that Flask knows
# what logic to execute when a client requests a given URL.

# A decorator modifies the function that follows it. A common pattern with decorators
# is to use them to register functions as callbacks for certain events.

# Creating mock objects is a useful technique that allows you to concentrate on one part of the
# application without having to worry about other parts of the system that don’t exist yet. I want
# to design the home page of my application, and I don’t want the fact that I don’t have a user
# system in place to distract me, so I just make up a user object so that I can keep going.