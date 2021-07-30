from flask import Flask
from pymongo import MongoClient
from pprint import pprint
import os


app = Flask(__name__)

client = MongoClient(os.environ.get('DATABASE_URL'))


@app.route('/')
def hello_world():
    return {"message": "Hello World"}
