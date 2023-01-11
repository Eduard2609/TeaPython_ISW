#uses tests/conftest.py fixture to test HERE in tests/functional/test_users.py
def test_home_page_post_with_fixture(test_client):

    #GIVEN a Flask application configured for testing
    #WHEN the '/' page is requested (POST)
    #THEN check that a 405 status code = is returned

    response = test_client.post('/')
    assert response.status_code == 405
    assert b'Home' not in response.data
  