from flask import render_template, redirect, url_for, request, Response
from application import app
import requests

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home:')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    get()
    post()
    return render_template('generate.html', title='Generate:')

def get():
    return Response(animal=requests.get('http://localhost:5001/animal'), mimetype='text/plain')

def post():
    return Response(noise=requests.post('http://localhost:5001/noise', data=animal), mimetype='text/plain')
