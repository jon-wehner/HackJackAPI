import os
from flask import Flask
from flask_jwt_extended import (create_access_token,
                                get_jwt_identity, jwt_required, JWTManager)
from pymongo import MongoClient
from pprint import pprint


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.environ.get('JWTSECRETKEY')
jwt = JWTManager(app)

client = MongoClient(os.environ.get('DATABASE_URL'))
db = client.admin

server_status_result = db.command("serverStatus")
pprint(server_status_result)


@app.route('/')
def hello_world():
    return {"message": "Hello World"}
