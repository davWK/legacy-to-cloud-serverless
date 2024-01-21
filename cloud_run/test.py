import unittest
from unittest.mock import patch, MagicMock
from bson.objectid import ObjectId
from app import app, todos
import mongomock
import flask

# Create a mock MongoDB instance
mock_db = mongomock.MongoClient().db

class TestApp(unittest.TestCase):
    def setUp(self):
        # Create a test client instance
        self.app = app.test_client()
        # Enable testing mode. Exceptions are propagated rather than handled by the the app's error handlers
        self.app.testing = True 

    def test_index_post(self):
        # Patch the insert_one method of todos with a MagicMock
        with patch('app.todos.insert_one', new_callable=MagicMock) as mock_insert_one:
            # Create a test request context for the app
            with app.test_request_context('/'):
                # Set the request method to 'POST'
                flask.request.method = 'POST'
                # Set the request form data
                flask.request.form = {'content': 'Test Content', 'degree': 'Test Degree'}
                # Send a POST request to the app
                result = self.app.post('/', data=flask.request.form)
                # Assert that the status code of the response is 302
                self.assertEqual(result.status_code, 302)
                # Assert that the insert_one method was called
                mock_insert_one.assert_called()