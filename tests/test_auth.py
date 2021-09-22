from py import test
import pytest
from app.api.auth import jwt, bcrypt, User
from app.db import delete_user

test_user = {
    'name': 'Bob Test',
    'email': 'bob@test.com',
    'password': 'password',
    'username': 'bob34'
}


@pytest.mark.auth
def test_jwt(client):
    test_jwt = jwt
    assert test_jwt is not None


@pytest.mark.auth
def test_registration(client):
    response = client.post('/api/auth/register', json={
        'username': test_user['username'],
        'email': test_user['email'],
        'name': test_user['name'],
        'password': test_user['password']
    })
    json = response.get_json()
    assert json["success"] == "User Registered"


@pytest.mark.auth
def test_login(client):
    success_response = client.post('/api/auth/login', json={
        'email': test_user['email'], 'password': test_user['password']
    })
    json = success_response.get_json()
    assert json["username"] == test_user['username']
    assert json["name"] == test_user['name']
    delete_user(test_user['email'])
