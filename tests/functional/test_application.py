from project import create_app

## FUNCTIONAL TESTS focus on how the view functions operate under different conditions (invalid http methods, invalid data, nominal conditions (GET, POST, PUT, DELETE), etc.)
def test_home_page():
    flask_app = create_app()

    # GIVEN a Flask application configured for testing
    # WHEN the '/' page is requested (GET)
    # THEN check that the response is valid


    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        response = testing_client.get('/')
        assert response.status_code == 200
        assert b'Home' in response.data
        assert b'About' in response.data
        assert b'Login' in response.data
        assert b'Register' in response.data

    
def test_home_post():

    #GIVEN a Flask application configured for testing
    #WHEN the '/' page is requested (POST)
    #THEN check that a 405 error is returned

    flask_app = create_app()
    #Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        response = testing_client.post('/')
        assert response.status_code == 405
        assert b'Home' not in response.data

## Testele se vor face cu interpretorul python3.6 sau python3.7 pentru path
## altfel pytest nu va reusi sa gaseasca souce code-ul
        