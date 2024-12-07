import logging
from flask import Flask, jsonify, request, make_response, Response
import models.api_model as api_model
import random
import os
from dotenv import load_dotenv
from utils.logger import configure_logger


# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Accessing environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_PATH')

# Example of using the Flask environment configuration
if __name__ == "__main__":
    app.run(debug=True)

# Initialize the API model
affirmation_model = api_model()

logger = logging.getLogger(__name__)
configure_logger(logger)

@app.before_request
def log_request_info():
    logger.info("Request: %s %s", request.method, request.url)

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
@app.route('/api/create-user', methods=['POST'])
def create_user() -> Response:
    """
    Route to create a new user.

    Expected JSON Input:
        - username (str): The username for the new user.
        - password (str): The password for the new user.

    Returns:
        JSON response indicating the success of user creation.
    Raises:
        400 error if input validation fails.
        500 error if there is an issue adding the user to the database.
    """
    app.logger.info('Creating new user')
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract and validate required fields
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return make_response(jsonify({'error': 'Invalid input, both username and password are required'}), 400)

        # Call the User function to add the user to the database
        app.logger.info('Adding user: %s', username)
        Users.create_user(username, password)

        app.logger.info("User added: %s", username)
        return make_response(jsonify({'status': 'user added', 'username': username}), 201)
    except Exception as e:
        app.logger.error("Failed to add user: %s", str(e))
        return make_response(jsonify({'error': str(e)}), 500)
    

@app.route('/api/login', methods=['POST'])
def login():
    """
    Route to log in a user and load their combatants.

    Expected JSON Input:
        - username (str): The username of the user.
        - password (str): The user's password.

    Returns:
        JSON response indicating the success of the login.

    Raises:
        400 error if input validation fails.
        401 error if authentication fails (invalid username or password).
        500 error for any unexpected server-side issues.
    """
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        app.logger.error("Invalid request payload for login.")
        raise BadRequest("Invalid request payload. 'username' and 'password' are required.")

    username = data['username']
    password = data['password']

    try:
        # Validate user credentials
        if not Users.check_password(username, password):
            app.logger.warning("Login failed for username: %s", username)
            raise Unauthorized("Invalid username or password.")

        # Get user ID
        user_id = Users.get_id_by_username(username)

        # Load user's combatants into the battle model
        login_user(user_id, battle_model)

        app.logger.info("User %s logged in successfully.", username)
        return jsonify({"message": f"User {username} logged in successfully."}), 200

    except Unauthorized as e:
        return jsonify({"error": str(e)}), 401
    except Exception as e:
        app.logger.error("Error during login for username %s: %s", username, str(e))
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/api/update-password', methods=['PUT'])
def update_password() -> Response:
    """
    Route to update a user's password.

    Expected JSON Input:
        - username (str): The username of the user.
        - new_password (str): The new password to set.

    Returns:
        JSON response indicating the success of the password update.
    Raises:
        400 error if input validation fails.
        404 error if the user does not exist.
        500 error if there is an issue updating the password in the database.
    """
    app.logger.info('Updating user password')
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract and validate required fields
        username = data.get('username')
        new_password = data.get('new_password')

        if not username or not new_password:
            return make_response(jsonify({'error': 'Invalid input, both username and new_password are required'}), 400)

        # Call the User function to update the password
        app.logger.info('Updating password for user: %s', username)
        Users.update_password(username, new_password)

        app.logger.info("Password updated for user: %s", username)
        return make_response(jsonify({'status': 'password updated', 'username': username}), 200)
    except ValueError as e:
        app.logger.error("Failed to update password: %s", str(e))
        return make_response(jsonify({'error': str(e)}), 404)
    except Exception as e:
        app.logger.error("Failed to update password: %s", str(e))
        return make_response(jsonify({'error': str(e)}), 500)


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
