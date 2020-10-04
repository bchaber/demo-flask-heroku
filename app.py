# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route('/about')
def about():
    return "It is a demo web application"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)