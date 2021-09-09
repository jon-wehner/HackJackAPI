import pytest
from app.db import add_user, delete_user, get_user


test_user = {
    'name': 'Bob Test',
    'email': 'bob@test.com',
    'hashed_password': 'password',
    'username': 'bob34'
}


@pytest.mark.users
def test_registration(client):
    delete_user(test_user['email'])
    response = add_user(test_user)
    assert response == {"success": "User Registered"}
    user = get_user(test_user['email'])
    assert user['email'] == test_user['email']


@pytest.mark.users
def test_duplicate_registration(client):
    response = add_user(test_user)
    assert response == {
        "error": "Email Already In Use"}
    delete_user(test_user['email'])
