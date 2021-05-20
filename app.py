import os
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = os.environ['SESSION_SECRET']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods = ['POST'])
def new():
    session['player'] = request.form['name']
    return redirect(url_for('play'))

@app.route('/play')
def play():
    return render_template('play.html', player=session['player'])

if __name__ == '__main__':
    app.run()
