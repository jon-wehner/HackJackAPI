import os
import bcrypt
from flask import Flask
from flask_jwt_extended import (create_access_token,
                                get_jwt_identity, jwt_required, JWTManager)
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from pprint import pprint
from .models import get_db

app = Flask(__name__)

bcrypt = Bcrypt(app)
CORS(app)

app.config['JWT_SECRET_KEY'] = os.environ.get('JWTSECRETKEY')
jwt = JWTManager(app)

pprint(get_db())


@app.route('/')
def hello_world():
    return {"message": "Hello World"}
