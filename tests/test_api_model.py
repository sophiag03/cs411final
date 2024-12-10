import unittest
from unittest.mock import patch, MagicMock
import requests
from models.api_model import AffirmationModel

class TestAffirmationModel(unittest.TestCase):

    def setUp(self):
        self.model = AffirmationModel()

    @patch('models.api_model.requests.get')
    def test_fetch_affirmation_success(self, mock_get):
        #mock an accomplished API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"affirmation": "You are amazing!"}
        mock_get.return_value = mock_response

        result = self.model.fetch_affirmation()

        self.assertEqual(result, "You are amazing!")
        self.assertIn("You are amazing!", self.model.affirmations)

    @patch('models.api_model.requests.get')
    def test_fetch_affirmation_no_affirmation(self, mock_get):
        #mock API response with no affirmation
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        result = self.model.fetch_affirmation()

        self.assertIsNone(result)
        self.assertEqual(len(self.model.affirmations), 0)

    @patch('models.api_model.requests.get')
    def test_fetch_affirmation_api_error(self, mock_get):
        #mock a failed API call
        mock_get.side_effect = requests.exceptions.RequestException("API error")

        result = self.model.fetch_affirmation()

        self.assertEqual(result, "API error")
        self.assertEqual(len(self.model.affirmations), 0)

    def test_get_all_affirmations(self):
        #add affirmations manually
        self.model.affirmations = ["Stay positive", "You got this"]

        result = self.model.get_all_affirmations()

        self.assertEqual(result, ["Stay positive", "You got this"])

    def test_clear_affirmations(self):
        #add affirmations manually and then clear them
        self.model.affirmations = ["Stay positive", "You got this"]
        self.model.clear_affirmations()

        self.assertEqual(len(self.model.affirmations), 0)

    def test_get_affirmation_count(self):
        #add affirmations manually and check the count
        self.model.affirmations = ["Stay positive", "You got this"]

        result = self.model.get_affirmation_count()

        self.assertEqual(result, 2)

    def test_fetch_multiple_affirmations(self):
        #mock fetching multiple affirmations
        self.model.affirmations = ["You are strong", "Keep going"]
        self.model.affirmations.append("You are amazing!")

        result = self.model.get_all_affirmations()
        self.assertEqual(len(result), 3)

    def test_clear_empty_affirmations(self):
        #clear affirmations when the list is already empty
        self.model.clear_affirmations()

        self.assertEqual(len(self.model.affirmations), 0)

    def test_initial_affirmation_count(self):
        #check affirmation count immediately after initialization
        self.assertEqual(self.model.get_affirmation_count(), 0)

if __name__ == '__main__':
    unittest.main()
