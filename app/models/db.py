import os
from flask import current_app, g
from werkzeug.local import LocalProxy
from pymongo import MongoClient
import pprint


def get_db():
    db = getattr(g, "_database", None)

    DB_URI = os.environ.get('DATABASE_URL')
    DB_NAME = os.environ.get('DATBASE_NAME')

    if db is None:
        db = g._database = MongoClient(DB_URI)[DB_NAME]

    return db
