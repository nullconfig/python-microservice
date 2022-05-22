import sys, pytest
from os import path
here = path.abspath(path.dirname(__file__))
sys.path.append(f"{here}/../../src")
from python_app.python_api_framework import app

class TestWebApp:
    '''
    Test class for ensuring the web application 
    returns expected response codes and data
    '''

    @pytest.fixture(scope="module")
    def test_app(self):
        '''
        Configures the app for testing
        Sets app config variable ``TESTING`` to ``True``
        :return: App for testing
        '''
        app.config['TESTING'] = True
        client = app.test_client()

        yield client

    def test_response(self, test_app):
        url = "/github/nullconfig"
        response = test_app.get(url)
        assert response.status_code == 200
        assert b'baseball' not in response.data
        assert b'ansible' in response.data

    def test_metrics(self, test_app):
        url = "/metrics"
        response = test_app.get(url)
        assert response.status_code == 200
        assert b'EOF' in response.data
