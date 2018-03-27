from flask import Flask

app = Flask(__name__)

from app import routes

# The script above simply creates the application object as an instance of class Flask imported from the flask package.
# The __name__ variable passed to the Flask class is a Python prede-
# fined variable, which is set to the name of the module in which it is used. Flask uses the location
# of the module passed here as a starting point when it needs to load associated resources such as
# template files, which I will cover in Chapter 2. For all practical purposes, passing __name__
# is almost always going to configure Flask in the correct way. The application then imports the
# routes module, which doesn’t exist yet.



# Another peculiarity is that the routes module is imported at the bottom and not at the top
# of the script as it is always done. The bottom import is a workaround to circular imports, a
# common problem with Flask applications. You are going to see that the routes module needs
# to import the app variable defined in this script, so putting one of the reciprocal imports at the
# bottom avoids the error that results from the mutual references between these two files.