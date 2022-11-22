import pytest

from project import create_app, db
from project.models import User, Suggestion


@pytest.fixture(scope='module')
def new_user():
    user = User('unit_test1', 'unit_test1@gmail.com', 'password', 'password') # username, email, password, confirm_password
    return user

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()
    