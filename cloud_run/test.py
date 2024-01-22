import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('app.db')
    def test_index_post(self, mock_db):
        mock_collection = MagicMock()
        mock_db.collection.return_value = mock_collection

        response = self.app.post('/', data={'content': 'Test Todo', 'degree': 'Test Degree'})

        mock_collection.add.assert_called_once_with({'content': 'Test Todo', 'degree': 'Test Degree'})
        self.assertEqual(response.status_code, 302)

    @patch('app.db')
    def test_delete(self, mock_db):
        mock_collection = MagicMock()
        mock_document = MagicMock()
        mock_collection.document.return_value = mock_document
        mock_db.collection.return_value = mock_collection

        response = self.app.post('/123/delete/')

        mock_document.delete.assert_called_once()
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()