from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# will have different urls for authentication pages
# like login page stored inside
auth = Blueprint('auth', __name__)

# when webiste is ran with either of these prefixes
# the following code will run
# ex if website.com/login is run, the login function will run
# and returns the html file/doc for the login page
@auth.route('/login', methods=['GET','POST']) 
def login():
    if request.method == 'POST': # after submitting the form on login page, following data is sent to server
        email = request.form.get('email')
        password = request.form.get('password')

        # grab the user from the db using the email inputted
        user = User.query.filter_by(email=email).first()
        if user: # if exists, check password
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) # remembers that this user is logged in for the flask session
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else: # else, error message
            flash('Email does not ezit.', category='error')

    return render_template("login.html", user=current_user) 
    # putting user as part of arguement will return if the current user is authenticated (in the db)
    # allowing certain tabs in navbar to be shown

@auth.route('/logout') 
@login_required # cannot access this route if not logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST': 
        # request method allows to get any forms submitted to server
        # from the form that was submitted in the html file
        # "request.get()" allows for specific access to certain attributes, differentiated through the "name" attribute of the field
        email = request.form.get('email') 
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # check if current user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        # flash message on screen if error occurs
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error') 
            # send error to user that email is invalid 
            # category can be 'success' or 'error'
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error') 
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256')) # creates User, puts password through hash function
            db.session.add(new_user) # adds user to database
            db.session.commit() # commits the changes to database
            login_user(user, remember=True) # remembers that this user is logged in for the flask session
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))


    return render_template("sign_up.html", user=current_user)