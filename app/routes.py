from app import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello world!"

# In Flask, handlers for the application routes are written as Python functions, called
# view functions. View functions are mapped to one or more route URLs so that Flask knows
# what logic to execute when a client requests a given URL.

# A decorator modifies the function that follows it. A common pattern with decorators
# is to use them to register functions as callbacks for certain events.