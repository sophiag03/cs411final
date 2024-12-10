import unittest
from unittest.mock import patch, MagicMock
import requests
from models.api_model import AffirmationModel

class TestAffirmationModel(unittest.TestCase):

    def setUp(self):
        self.model = AffirmationModel()

    @patch('models.api_model.requests.get')
    def test_fetch_affirmation_success(self, mock_get):
        # Mock a successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"affirmation": "You are amazing!"}
        mock_get.return_value = mock_response

        result = self.model.fetch_affirmation()

        self.assertEqual(result, "You are amazing!")
        self.assertIn("You are amazing!", self.model.affirmations)

    @patch('models.api_model.requests.get')
    def test_fetch_affirmation_no_affirmation(self, mock_get):
        # Mock an API response with no affirmation
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        result = self.model.fetch_affirmation()

        self.assertIsNone(result)
        self.assertEqual(len(self.model.affirmations), 0)

    @patch('models.api_model.requests.get')
    def test_fetch_affirmation_api_error(self, mock_get):
        # Mock a failed API call
        mock_get.side_effect = requests.exceptions.RequestException("API error")

        result = self.model.fetch_affirmation()

        self.assertEqual(result, "API error")
        self.assertEqual(len(self.model.affirmations), 0)

    def test_get_all_affirmations(self):
        # Add affirmations manually
        self.model.affirmations = ["Stay positive", "You got this"]

        result = self.model.get_all_affirmations()

        self.assertEqual(result, ["Stay positive", "You got this"])

    def test_clear_affirmations(self):
        # Add affirmations manually and then clear them
        self.model.affirmations = ["Stay positive", "You got this"]
        self.model.clear_affirmations()

        self.assertEqual(len(self.model.affirmations), 0)

    def test_get_affirmation_count(self):
        # Add affirmations manually and check the count
        self.model.affirmations = ["Stay positive", "You got this"]

        result = self.model.get_affirmation_count()

        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
