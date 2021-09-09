from re import L
import pytest
from app.api.auth import jwt, get_bcrypt, User


@pytest.mark.auth
def test_jwt(client):
    test_jwt = jwt
    assert test_jwt is not None
