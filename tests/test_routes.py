import unittest
from app import create_app, db
from app.config import TestConfig

class PetPalTestCase(unittest.TestCase):
    def setUp(self):
        # Creates a new Flask application for testing
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

        # Set up your database and other necessary setup steps here
        db.create_all()

    def tearDown(self):
        # Tear down your database and other cleanup steps here
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        # Example test for the home page route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Welcome to PetPal' in response.get_data(as_text=True))

# Add more tests as needed

if __name__ == '__main__':
    unittest.main()
