import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt


def create_app(test_config=None):
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = os.environ.get('JWTSECRETKEY')
    app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')
    app.config['DATABASE_NAME'] = os.environ.get('DATABASE_NAME')
    app.config['BCRYPT'] = Bcrypt(app)

    jwt = JWTManager(app)

    CORS(app)

    return app
