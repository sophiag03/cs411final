# Affirmation Generator

## Overview
The Affirmation Generator is designed to provide users with positive affirmation quotes. The application generates and outputs a random affirmation to motivate users and improve their overall mood. Users can also keep track of how many affirmations they have received from the application and view all previous affirmations sent to them.

**API:** [https://www.affirmations.dev/](https://www.affirmations.dev/)

---

## Features
- **Fetch a New Affirmation**: Retrieves a new affirmation from an external API and stores it in memory for future use.
- **View All Affirmations**: Displays all stored affirmations, allowing users to review their gathered affirmations.
- **Clear All Affirmations**: Deletes all stored affirmations, providing a clean slate for users.
- **Get Affirmation Count**: Returns the total number of affirmations currently stored in memory.
- **Retrieve a Random Affirmation**: Fetches a random affirmation from the stored affirmations for an element of surprise.

---

## API Endpoints

### **Route: `/create-user`**
- **Request Type:** POST  
- **Purpose:** Creates a new user account with a username and password.  
- **Request Body:**
    {
        "username": "newuser123",
        "password": "securepassword"
    }
- **Reponse Format:** JSON
- **Success Reponse Example:**
    - Code: 200
    - Content: { "message": "Account created successfully" }
- **Example Request:**
    {
        "username": "newuser123",
        "password": "securepassword"
    }
- **Example Response:**
    {
        "message": "Account created successfully",
        "status": "200"
    }