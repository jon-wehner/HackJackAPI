from flask import Blueprint, current_app, g, request
from werkzeug.local import LocalProxy
from app.db import add_user

auth = Blueprint('auth', __name__, url_prefix='/auth')

jwt = current_app.config['JWT']
bcrypt = current_app.config['BCRYPT']


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
    hashed_password = bcrypt.generate_password_hash.get_data['password']

    user = add_user(User(username, email, name, hashed_password))
    return user
