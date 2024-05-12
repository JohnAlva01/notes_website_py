# store routes for website
# aka login, home page
# any route that users can access

from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

# blueprint of app, urls stored in the blueprint
# can have url split up in separate files
views = Blueprint('views', __name__)

# when '/' route is typed in after url, like 'app.com/'
# the following function 'home' will run
@views.route('/', methods=['GET', 'POST'])
@login_required # can't access homepage if login isn't achieved
def home():
    # renders the html file called home.html
    if request.method == 'POST': # if the server receives a post request
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note/', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})