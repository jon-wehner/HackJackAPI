from flask import Flask
from pymongo import MongoClient
from pprint import pprint
import os


app = Flask(__name__)

client = MongoClient(os.environ.get('DATABASE_URL'))
db = client.admin

server_status_result = db.command("serverStatus")
pprint(server_status_result)


@app.route('/')
def hello_world():
    return {"message": "Hello World"}
