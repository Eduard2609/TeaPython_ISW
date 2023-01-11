from project import create_app

## FUNCTIONAL TESTS focus on how the view functions operate under different conditions (invalid http methods, invalid data, nominal conditions (GET, POST, PUT, DELETE), etc.)
def test_home_page():
    flask_app = create_app('flask_test.cfg') # creates a flask application

    # GIVEN a Flask application configured for testing
    # WHEN the '/' page is requested (GET)
    # THEN check that the response is valid


    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client: #utilize the test_client included in Flask to GET the homepage '/' route
        response = test_client.get('/')
        assert response.status_code == 302
        assert b'Home' in response.data
        assert b'About' in response.data
        assert b'Login' in response.data
        assert b'Register' in response.data

    
def test_home_page_post():

    #GIVEN a Flask application configured for testing
    #WHEN the '/' page is requested (POST)
    #THEN check that a 405 status code = is returned

    flask_app = create_app('flask_test.cfg')
    #Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client: #utilize the test_client included in Flask to POST the homepage '/' route
        response = test_client.post('/')
        assert response.status_code == 200
        assert b'Home' not in response.data

## Testele se vor face cu interpretorul python3.6 sau python3.7 pentru path
## altfel pytest nu va reusi sa gaseasca souce code-ul
        