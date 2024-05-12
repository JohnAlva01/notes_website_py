from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy() # creates the database to store user information
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'helfdjksalfdas' # saves the cookie data 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # sqlalchemy database is stored at location "sqlite:///database.db"
    db.init_app(app) # tells database what app is using the database

    # can import the different blueprints made
    # from their respective .py files
    from .views import views
    from .auth import auth

    # url prefix means that the defined prefix
    # has to be typed to access the route
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Note
    from .models import User
    # defines the models before creating the database
    with app.app_context():
        db.create_all()
        # creates database with the app

    login_manager = LoginManager()
    # where to go if not logged in
    # where should flask redirect if login is required
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) 
        # .get knows its going to look for the primary id
        # referencing by id

    return app

