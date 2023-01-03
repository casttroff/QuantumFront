from flask import Flask, render_template, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response(redirect('/home'))
    return response

@app.route('/home')
def home():
    return render_template('home.html') 

if __name__ == '__main__':
    app.run()
