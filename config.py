import os
from app import app

BASE_DIR = os.path.abspath(os.path.dirname(__file__) + '/app')

DEBUG = True

CSRF_ENABLED = True

THREADS_PER_PAGE = 2

CSRF_SESSION_KEY = os.environ['SESSION_SECRET']

SESSION_SECRET = os.environ['SESSION_SECRET']

app.secret_key = SESSION_SECRET
