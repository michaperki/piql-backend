import unittest
from app import create_app, db

class TestRoutes(unittest.TestCase):
    def setUp(self):
        # Create a test client and app context
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Initialize the test database (if you are using one)
        db.create_all()

    def tearDown(self):
        # Clean up the database and app context
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_root_route(self):
        # Send a GET request to the root route
        response = self.client.get('/')

        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
