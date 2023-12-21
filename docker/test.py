import unittest
from unittest.mock import patch, MagicMock
from bson.objectid import ObjectId
from app import app, todos
import mongomock
import flask

mock_db = mongomock.MongoClient().db

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_index_post(self):
        with patch('app.todos.insert_one', new_callable=MagicMock) as mock_insert_one:
            with app.test_request_context('/'):
                flask.request.method = 'POST'
                flask.request.form = {'content': 'Test Content', 'degree': 'Test Degree'}
                result = self.app.post('/', data=flask.request.form)
                self.assertEqual(result.status_code, 302)
                mock_insert_one.assert_called()

