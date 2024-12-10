
import requests
import logging

from utils.logger import configure_logger


logger = logging.getLogger(__name__)
configure_logger(logger)

class AffirmationModel:
    def __init__(self):
       """
        Initializes the AffirmationManager instance with an empty list for affirmations.

        Args:
            None

        Returns:
            None
        """
       self.affirmations = []

    def fetch_affirmation(self):
        """
        Fetches a random affirmation from the external API and stores it in memory.

        Args:
            None

        Returns: 
            The fetched affirmation as a string if the API call is successful,
            or `None` if no affirmation is retrieved.

        Raises:
            A string describing the exception if an HTTP request error occurs.
        """
        try:
            response = requests.get('https://www.affirmations.dev/')
            if response.status_code == 200:
                affirmation = response.json().get('affirmation')
                if affirmation:
                    self.affirmations.append(affirmation)
                    return affirmation
            return None
        except requests.exceptions.RequestException as e:
            return str(e)

    def get_all_affirmations(self):
        """
        Returns all stored affirmations.

        Args:
            None

        Returns:
            A list of all stored affirmations.
        """
        return self.affirmations

    def clear_affirmations(self):
        """
        Clears all stored affirmations.

        Args:
            None

        Returns:
            None
        """
        self.affirmations = []

    def get_affirmation_count(self):
        """
        Returns the count of affirmations stored in memory.

        Args:
            None

        Returns:
            An integer representing the number of affirmations stored.
        """
        return len(self.affirmations)
