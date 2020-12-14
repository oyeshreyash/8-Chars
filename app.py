from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('base.html')

@app.route('/gen')
def pass_show():
    letters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    rand_letters = random.choices(letters, k = 8)
    rand_letters = "".join(rand_letters)
    gen_pw = rand_letters
    return render_template('base.html', display_password=gen_pw)

if __name__ == '__main__':
    app.run(debug=True)

