* In Python, a sub-directory that includes a __init__.py
file is considered a package, and can be imported.
* When you import a package, the __init__.py
executes and defines what symbols the package exposes to the outside world.


## Flask settings

There are several formats for the application to specify configuration options. The most basic
solution is to define your variables as keys in app.config , which uses a dictionary style to
work with variables.

```flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
# ... add more variables here as needed
```


Separation oif concepts version:

```
file: config.py: Secret key configuration

import os
class Config(object):
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
```

The configuration settings are defined as class variables inside the Config
class. As the application needs more configuration items, they can be added to this class, and later if I find that I need to have more than one configuration set, I can create subclasses of it.
But don’t worry about this just yet.


must do 
export FLASK_APP=microblog.py
