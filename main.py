
from flask import Flask, render_template

app = Flask(__name__)

flashcards = [
    {
        "front": "Fair dinkum",
        "back": "Echt waar"
    },
    {
        "front": "She'll be right, mate",
        "back": "Het komt wel goed, maat"
    },
    {
        "front": "No worries",
        "back": "Geen probleem"
    },
    {
        "front": "Chuck a shrimp on the barbie",
        "back": "Gooi een garnaal op de barbecue"
    },
    {
        "front": "Full of beans",
        "back": "Vol energie"
    }
]

@app.route('/')
def index():
    return render_template('index.html', flashcards=flashcards)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
