from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return f"<h1> Welcome </h1>"

@app.route('/welcome/home')
def welcome_home():
    return f"<h1> Welcome Home </h1>"

@app.route('/welcome/back')
def welcome_back():
    return f"<h1> Welcome Back </h1>"