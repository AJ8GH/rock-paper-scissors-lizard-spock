import os
from flask import Flask
from flask import render_template, redirect, url_for, request, session

from .models import Player, Game


app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods = ['POST'])
def new():
    session['player'] = request.form.get('name', 'human')
    return redirect(url_for('play'))

@app.route('/play')
def play():
    player = Player(session.get('player', 'human'))
    game = Game(player)
    return render_template('play.html', game=game)
