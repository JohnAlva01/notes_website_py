from flask import Blueprint

# will have different urls for authentication pages
# like login page stored inside
auth = Blueprint('auth', __name__)

# when webiste is ran with either of these prefixes
# the following code will run
# ex if website.com/login is run, the login function will run
# and returns the html file/doc for the login page
@auth.route('/login') 
def login():
    return "<p>Login</p>"

@auth.route('/logout') 
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up') 
def sign_up():
    return "<p>Sign Up</p>"