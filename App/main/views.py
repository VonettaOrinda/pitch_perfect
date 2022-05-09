from crypt import methods
from json.tool import main
from os import abort
from turtle import title

from flask import redirect, render_template, url_for
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

@main.route('/create_new', methods=['POST''GET'])
@login_required
def new_pitch():
    form=PitchForm()
    if form.validate_on_submit():
        title=form.title.data
        post=form.post.data
        category=form.category.data
        user_id=current_user
        new_pitch_object=Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for(main.index))
    
    return render_template('create_pitch.html', form=form)
    





@main.route('/user/<name>')
def profile(name):
    user.query.filter_by(username=name).first()
    user_id=current_user._get_current_object().id
    posts=pitch.query.filter_by(user_id=user_id).all()
    if user is None:
        abort(404)
        
    return render_template("profile/profile.html", user=user, posts=posts)
    
    
    
    