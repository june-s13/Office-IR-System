import unittest
from unittest.mock import patch, MagicMock
from flask_testing import TestCase
from app import app
import numpy as np

class TestFlaskApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    @patch('builtins.open', unittest.mock.mock_open(read_data="mocked data"))
    @patch('pickle.load')
    def test_query_endpoint(self, mock_pickle_load):
        vectorizer = MagicMock()
        tfidf_matrix = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
        # Adjust the return value to match the dimensions of the tfidf_matrix
        vectorizer.transform.return_value = np.array([[0.5, 0.5, 0.5]])  # 2D array with one sample and three features
        mock_pickle_load.return_value = (vectorizer, tfidf_matrix)

        response = self.client.post('/query', json={'query': 'test', 'k': 5})
        print(response.json)  # Debug output to check the error message
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
