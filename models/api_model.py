
import requests

class AffirmationModel:
    def __init__(self):
       
        self.affirmations = []

    def fetch_affirmation(self):
        """
        Fetches a random affirmation from the external API and stores it in memory.
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
        """
        return self.affirmations

    def clear_affirmations(self):
        """
        Clears all stored affirmations.
        """
        self.affirmations = []

    def get_affirmation_count(self):
        """
        Returns the count of affirmations stored in memory.
        """
        return len(self.affirmations)
