# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'student'}
    posts = [
        {
            'author':{'username': 'John'},
            'body': 'Beautiful day in Vinnica!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Василий'},
            'body':'Привеееет!!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
