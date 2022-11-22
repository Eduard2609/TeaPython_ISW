from project import create_app

def test_home_page():
    flask_app = create_app()

    with flask_app.test_client() as testing_client:
        response = testing_client.get('/')
        assert response.status_code == 200
        assert b'Home' in response.data
        assert b'About' in response.data
        assert b'Login' in response.data
        assert b'Register' in response.data

    
def test_home_post():
    flask_app = create_app()

    with flask_app.test_client() as testing_client:
        response = testing_client.post('/')
        assert response.status_code == 405
        assert b'Home' not in response.data
        