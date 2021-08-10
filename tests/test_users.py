import pytest
from app.db import add_user, delete_user, get_user


test_user = {
    'name': 'Bob Test',
    'email': 'bob@test.com',
    'hashedpassword': 'password',
    'username': 'bob34'
}


@pytest.mark.users
def test_registration(client):
    delete_user(test_user['email'])
    add_user(test_user)

    user = get_user(test_user['email'])
    assert user.email == test_user['email']
