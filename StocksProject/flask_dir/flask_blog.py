# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:05:22 2020

@author: NjordSoevik
"""

from flask import Flask, render_template
app = Flask(__name__)

postslist = [{
        'author':'someone',
        'title':'story 1!'
        },
        {
        'author':'someone',
        'title':'story 2!'
        }]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=postslist,title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='Home')

if __name__ == '__main__':
    app.run(debug=True) 