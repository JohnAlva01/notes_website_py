# store routes for website
# aka login, home page
# any route that users can access

from flask import Blueprint, render_template

# blueprint of app, urls stored in the blueprint
# can have url split up in separate files
views = Blueprint('views', __name__)

# when '/' route is typed in after url, like 'app.com/'
# the following function 'home' will run
@views.route('/')
def home():
    # renders the html file called home.html
    return render_template("home.html")
