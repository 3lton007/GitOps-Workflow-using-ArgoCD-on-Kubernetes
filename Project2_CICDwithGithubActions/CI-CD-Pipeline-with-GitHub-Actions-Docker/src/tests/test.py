import unittest
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

class SimpleFlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('message', data)

    def test_health_route(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')

    def test_info_route(self):
        response = self.app.get('/info')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('Application', data)

    def test_sample_data_route(self):
        response = self.app.get('/api/data')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['count'], 3)

    def test_echo_route_get(self):
        response = self.app.get('/api/echo?param=value')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['method'], 'GET')
        self.assertEqual(data['args']['param'], 'value')

    def test_echo_route_post(self):
        test_data = {'test': 'hello'}
        response = self.app.post('/api/echo',
                               data=json.dumps(test_data),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['method'], 'POST')
        self.assertEqual(data['json_data'], test_data)

if __name__ == '__main__':
    unittest.main()