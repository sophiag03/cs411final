from flask import Flask, jsonify
import api_model
import random

app = Flask(__name__)

# Initialize the API model
affirmation_model = api_model()

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check route to verify the app is running.
    """
    return jsonify({"status": "App is running"}), 200

"""
need:

create account
login
update password

"""

@app.route('/fetch-affirmation', methods=['POST'])
def fetch_affirmation():
    """
    Fetches a new affirmation from the external API and stores it in memory.
    """
    affirmation = affirmation_model.fetch_affirmation()
    if affirmation:
        return jsonify({"message": "Affirmation fetched and stored.", "affirmation": affirmation}), 201
    else:
        return jsonify({"error": "Failed to fetch affirmation."}), 500

@app.route('/view-affirmations', methods=['GET'])
def view_affirmations():
    """
    Returns all stored affirmations.
    """
    affirmations = affirmation_model.get_all_affirmations()
    return jsonify({"affirmations": affirmations}), 200

@app.route('/clear-affirmations', methods=['DELETE'])
def clear_affirmations():
    """
    Clears all stored affirmations.
    """
    affirmation_model.clear_affirmations()
    return jsonify({"message": "All affirmations cleared."}), 200

@app.route('/affirmation-count', methods=['GET'])
def affirmation_count():
    """
    Returns the number of affirmations stored in memory.
    """
    count = affirmation_model.get_affirmation_count()
    return jsonify({"count": count}), 200

@app.route('/random-affirmation', methods=['GET'])
def random_affirmation():
    """
    Returns a random affirmation from the stored affirmations.
    """
    affirmations = affirmation_model.get_all_affirmations()
    if affirmations:
        random_affirmation = random.choice(affirmations)
        return jsonify({"affirmation": random_affirmation}), 200
    else:
        return jsonify({"message": "No affirmations available."}), 404

if __name__ == '__main__':
    app.run(debug=True)
