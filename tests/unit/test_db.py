from project.models import User
from project.models import Suggestion
from project.models import Application

#UNIT TESTS focus on testing small units of code in isolation
#UNIT TESTS are used to test the functionality of a single function or method for example : database models, utility functions called by view functions



def test_user():
    user = User(username = 'test', email = 'test@gmail.com', password = 'test')
    assert user.username == 'test'
    assert user.email == 'test@gmail.com'
    assert user.password == 'test'

#make another test for Sugesstion



def test_suggestion():
    suggestion = Suggestion(name = 'test', description = 'test', genre = 'test', install_command = 'test', image_file = 'test')
    assert suggestion.name == 'test'
    assert suggestion.description == 'test'
    assert suggestion.genre == 'test'
    assert suggestion.install_command == 'test'
    assert suggestion.image_file == 'test'

#make another test for Application 



def test_application():
    application = Application(name = 'test', description = 'test', genre = 'test', install_command = 'test', image_file = 'test')
    assert application.name == 'test'
    assert application.description == 'test'
    assert application.genre == 'test'
    assert application.install_command == 'test'
    assert application.image_file == 'test'

