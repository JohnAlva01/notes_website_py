from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'helfdjksalfdas' # saves the cookie data 

    # can import the different blueprints made
    # from their respective .py files
    from .views import views
    from .auth import auth

    # url prefix means that the defined prefix
    # has to be typed to access the route
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


