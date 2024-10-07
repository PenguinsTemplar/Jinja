from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('spell/<word>')
def spell_word(word):
    return render_template('spell_word.html', word=word)

if __name__ == '__main__':
    app.run(debug=True)