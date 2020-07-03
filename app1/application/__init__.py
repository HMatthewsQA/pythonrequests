from flask import Flask
import requests

api = 'http://localhost:5000'
app = Flask(__name__)

from application import routes
