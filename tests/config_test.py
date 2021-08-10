import pytest
from app import create_app

import os


@pytest.fixture
def app():
    app = create_app()
    app.config['JWT_SECRET_KEY'] = os.environ.get('TEST_SECRET_KEY')
    app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')
    app.config['DATABASE_NAME'] = os.environ.get('TEST_DATABASE_NAME')
    return app
