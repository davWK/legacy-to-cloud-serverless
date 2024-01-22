import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('app.todos.add')
    def test_index_post(self, mock_add):
        response = self.app.post('/', data={'content': 'Test Todo', 'degree': 'Test Degree'})

        mock_add.assert_called_once_with({'content': 'Test Todo', 'degree': 'Test Degree'})
        self.assertEqual(response.status_code, 302)

    @patch('app.todos.document')
    def test_delete(self, mock_document):
        mock_delete = MagicMock()
        mock_document.return_value.delete = mock_delete

        response = self.app.post('/123/delete/')

        mock_delete.assert_called_once()
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()