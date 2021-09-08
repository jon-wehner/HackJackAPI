import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from app.api.auth import auth


def create_app(test_config=None):
    app = Flask(__name__)

    jwt = JWTManager(app)
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWTSECRETKEY')
    app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')
    app.config['DATABASE_NAME'] = os.environ.get('DATABASE_NAME')
    app.config['BCRYPT'] = Bcrypt(app)
    app.config['JWT'] = jwt

    CORS(app)
    app.register_blueprint(auth)

    return app
