from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from random import choice, sample


app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = "Snapy23Clawn"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/greet')
def say_hello():
    """Say hello and prompt for user's name."""

    return render_template("greet.html")

@app.route('/old-home-page')
def redirect_to_home():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

