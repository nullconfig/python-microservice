import unittest
import subprocess
import http.client
import random
import time

class WebTestCase(unittest.TestCase):
    '''tests for the api microservice'''

    def setUp(self):
        self.server_process = subprocess.Popen(
            [
                "python",
                "python-api-exec.py"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        time.sleep(.25)

    def tearDown(self):
        self.server_process.kill()
        self.server_process.communicate()

    def get_response(self, url):
        '''
        Helper function to get a response from a given url, using http.client
        '''

        conn = http.client.HTTPConnection('localhost:8000')
        conn.request('GET', url)

        response = conn.getresponse()
        self.assertEqual(200, response.getcode())

        conn.close()

        return response

if __name__ == '__main__':
    unittest.main()
