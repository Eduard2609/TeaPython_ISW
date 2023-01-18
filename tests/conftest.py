
from project import create_app
import pytest
from project import  db
from project.models import User, Suggestion
from project.installscript.install import generate_bat_file
#FIXTURES are used to setup and teardown test data

@pytest.fixture(scope='module')
def new_user():
    user = User('patrickbateman68@gmail.com', 'FluffyBunny') #password is hashed
    return user

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    #create a test client using the flask app configured for testing
    with flask_app.test_client() as testing_client:
        #establish an application context
            yield testing_client #this is where the testing happens!

# @pytest.fixture(scope='module')
# def new_user():
#     user = User('unit_test1', 'unit_test1@gmail.com', 'password', 'password') # username, email, password, confirm_password
#     return user

# @pytest.fixture(scope='module')
# def test_client():
#     flask_app = create_app()
#     testing_client = flask_app.test_client()
#     ctx = flask_app.app_context()
#     ctx.push()
#     yield testing_client
#     ctx.pop()

@pytest.fixture(scope='module')
def test_bat_file():
    bat_file = generate_bat_file('test')
    return bat_file

