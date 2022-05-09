from json.tool import main

from flask import render_template
from ...models import pitch,comments,user,Upvote,Downvote
from .form import PitchForm,CommentForm,UpdateProfile
from flask import render_template

@main.route('/')
def index():
    pitch=pitch.query.all()
    elevator=pitch.query.filter_by(category='elevator').all()
    followup=pitch.query.filter_by(category='followup').all()
    email=pitch.query.filter_by(category='email').all()
    return render_template('index.html', elevator=elevator, followup=followup, email=email)
    
    
    