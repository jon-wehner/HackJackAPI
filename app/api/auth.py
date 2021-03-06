from flask import Blueprint, current_app, g, jsonify, request
from werkzeug.local import LocalProxy
from app.db import add_user, get_user
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__, url_prefix='/api/auth')


def get_jwt():
    jwt = getattr(g, '_jwt', None)
    if jwt is None:
        jwt = g._jwt = current_app.config['JWT']
    return jwt


def get_bcrypt():
    bcrypt = getattr(g, '_bcrypt', None)
    if bcrypt is None:
        bcrypt = g._bcrypt = current_app.config['BCRYPT']
    return bcrypt


jwt = LocalProxy(get_jwt)
bcrypt = LocalProxy(get_bcrypt)


class User():
    def __init__(self, username, email, name, hashed_password):
        self.username = username
        self.email = email
        self.name = name
        self.hashed_password = hashed_password

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "hashed_password": self.hashed_password
        }


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    name = data['name']
    password = data['password']
    confirm_password = data['confirmPassword']
    check_user = get_user(email)
    if check_user is not None:
        return {"error": "User already exists"}
    if password != confirm_password:
        return {"error": "Password fields must match"}
    hashed_password = bcrypt.generate_password_hash(data['password'])
    new_user = User(username, email, name, hashed_password)
    response = add_user(new_user.to_dict())
    return response


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = get_user(email)
    if user is not None and bcrypt.check_password_hash(
            user['hashed_password'], password):
        access_token = create_access_token(identity=user['username'])
        return jsonify(username=user['username'],
                       name=user['name'], access_token=access_token)
    else:
        return {"error": "Invalid Credentials"}
