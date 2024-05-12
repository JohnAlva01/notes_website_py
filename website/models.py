from . import db # actually importing the db object created in __init__.py
from flask_login import UserMixin
from sqlalchemy.sql import func


# creating models for database using sqlalchemy
# a db.Model is a schematic for the type of object that will be stored in the database
# ex. all Users have to conform to the User class


# database model for NOTES of users
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # how to associate a note with a user
    # using a foreign key, basically a reference to specific id of user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # db.ForeignKey ensures that we pass a valid ID number of an existing user
    # allows relationship between which note belongs to which user
    # FOREIGNKEY ONLY for one to many relationships (one user having many notes)


# database model for USERS
class User(db.Model, UserMixin):
    # create layout for User object which contains certain columns / fields
    id = db.Column(db.Integer, primary_key=True) # a unique integer identifier differentiating all accounts from each other
    email = db.Column(db.String(150), unique=True) # when unique is defined, no user can have the same email
    password = db.Column(db.String(150)) # max length of password is 150
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # tell SQLAlchemy that when new note is created, add that note ID to the relationship
    
# database is setup but NOT initialized