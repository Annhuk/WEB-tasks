import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_user(self):
        response = self.app.get('/user/1')
        self.assertEqual(response.status_code, 200)

    def test_user_not_found(self):
        response = self.app.get('/user/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()