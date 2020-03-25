from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Please dont copy this. Just an exp'

from app import routes
