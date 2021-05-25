from flask import Flask
from .models.player import Player

from flask import render_template, redirect, url_for, request, session

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods = ['POST'])
def new():
    session['player'] = request.form['name']
    return redirect(url_for('play'))

@app.route('/play')
def play():
    player = Player(session['player'])
    return render_template('play.html', player=player)
