import pytest
from app import create_app
from app.db import get_db
from werkzeug.local import LocalProxy

import os


@pytest.fixture
def client():
    app = create_app()
    app.config['JWT_SECRET_KEY'] = os.environ.get('TEST_SECRET_KEY')
    app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')
    app.config['DATABASE_NAME'] = os.environ.get('TEST_DATABASE_NAME')
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture
def db():
    app = create_app()
    app.config['JWT_SECRET_KEY'] = os.environ.get('TEST_SECRET_KEY')
    app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')
    app.config['DATABASE_NAME'] = os.environ.get('TEST_DATABASE_NAME')
    with app.test_client() as client:
        with app.app_context():
            yield client, db
