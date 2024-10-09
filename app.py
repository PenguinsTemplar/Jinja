from flask import Flask, request, render_template
from random import choice, sample


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route('/form-2')
def show_form_2():
    return render_template("form-2.html")

COMPLIMENTS = ["Cool","Suave","Simple","Indiferent"]

@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)

@app.route('/greet-2')
def get_greeting_2():
    username = request.args["username"]
    wants = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)
    return render_template("greet-2.html", username=username, wants_compliments=wants, compliments=nice_things)


@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word = caps_word)

if __name__ == '__main__':
    app.run(debug=True)