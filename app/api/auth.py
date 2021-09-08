from flask import Blueprint, current_app, g, request
from werkzeug.local import LocalProxy
from app.db import add_user

auth = Blueprint('auth', __name__, url_prefix='/auth')


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


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    name = data['name']
    hashed_password = bcrypt.generate_password_hash(data['password'])

    user = add_user(User(username, email, name, hashed_password))
    return user
