from flask import current_app, g
from werkzeug.local import LocalProxy
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


def get_db():
    db = getattr(g, "_database", None)

    DB_URI = current_app.config['DATABASE_URL']
    DB_NAME = current_app.config['DATBASE_NAME']

    if db is None:
        db = g._database = MongoClient(DB_URI)[DB_NAME]

    return db


db = LocalProxy(get_db)


def get_user(email):
    user = db.users.findOne({"email": email})
    return user


def add_user(user):
    try:
        db.users.insert_one({
            "username": user['username'],
            "name": user['name'],
            "email": user['email'],
            "password": user['hashedpassword'],
            "chips": 100
        }, {"writeConcern": "majority"})
        return {"success": "User Registered"}
    except DuplicateKeyError:
        return {"error": "Users Must have unique Email addresses"}


def delete_user(email):
    db.users.deleteOne(email)
