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

## Route Documentation

### **Route: `/create-user`**
- **Request Type:** POST  
- **Purpose:** Creates a new user account with a username and password.  
- **Request Body:**
    - username (String): User's chosen username.
    - password (String): User's chosen password.
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

### **Route: `/login`**
- **Request Type:** POST  
- **Purpose:** Logs a user into their account. 
- **Request Body:**
    - username (String): User's chosen username.
    - password (String): User's chosen password.
- **Reponse Format:** JSON
- **Success Reponse Example:**
    - Code: 200
    - Content: { "message": "User logged in successfully" }
- **Example Request:**
    {
        "username": "newuser123",
        "password": "securepassword"
    }
- **Example Response:**
    {
        "message": "User logged in successfully",
        "status": "200"
    }

### **Route: `/update-password`**
- **Request Type:** PUT
- **Purpose:** Updates the password of a user account
- **Request Body:**
    - username (String): User's chosen username.
    - new_password (String): User's chosen new password.
- **Reponse Format:** JSON
- **Success Reponse Example:**
    - Code: 200
    - Content: { "message": "Password updated for user" }
- **Example Request:**
    {
        "username": "newuser123",
        "new_password": "secure password"
    }
- **Example Response:**
    {
        "message": "Password updated for user",
        "status": "200"
    }

### **Route: `/fetch-affirmation`**
- **Request Type:** GET
- **Purpose:** Fetches a new affirmation from the external API and stores it in memory.
- **Parameters:**
    - String
- **Reponse Format:** JSON
- **Success Reponse Example:**
    - Code: 201
    - Content: { "message": "Affirmation fetched and stored.", “affirmation”: a random affirmation }
- **Example Response:**
    {
        "message": "Affirmation fetched and stored.r",
        "affirmation": "You are the best!"
        "status": "201"
    }

### **Route: `/view-affirmations`**
- **Request Type:** GET
- **Purpose:** Retrieves all previously stored affirmations.
- **Parameters:**
    - List
- **Reponse Format:** JSON
- **Success Reponse Example:**
    - Code: 200
    - Content: { "message": "Here are all your affirmations!", "affirmations": [ "You are capable of achieving great things.", "Believe in yourself.", "Every day is a new opportunity." ] }
- **Example Response:**
    {
        "message": "Here are all your affirmations!",
        "affirmations": [
            "You are capable of achieving great things.",
            "Believe in yourself.",
            "Every day is a new opportunity."
        ],
        "status": "200"
    }

### **Route: `/clear-affirmations`**
- **Request Type:** DELETE
- **Purpose:** Deletes all stored affirmations.
- **Parameters:**
    - None
- **Reponse Format:** JSON
- **Success Reponse Example:**
    - Code: 200
    - Content: { "message": "All affirmations cleared." }
- **Example Response:**
    {
        "message": "All affirmations cleared.",
        "status": "200"
    }

### **Route: `/affirmation-count`**
- **Request Type:** GET
- **Purpose:** Returns the number of affirmations stored in memory.
- **Parameters:**
    - Integer
- **Reponse Format:** JSON
- **Success Reponse Example:**
    - Code: 200
    - Content: { "count": number of stored affirmations }
- **Example Response:**
    {
        "count": 15,
        "status": "200"
    }

### **Route: `/random-affirmation`**
- **Request Type:** GET
- **Purpose:** Returns a random affirmation from the stored affirmations.
- **Parameters:**
    - String
- **Reponse Format:** JSON
- **Success Reponse Example:**
    - Code: 200
    - Content: { "affirmation": a random affirmation from memory }
- **Example Response:**
    {
        "affirmation": "You are capable of achieving great things.",
        "status": "200"
    }