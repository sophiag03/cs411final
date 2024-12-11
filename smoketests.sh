#!/bin/bash
BASE_URL="http://localhost:5001/api"

ECHO_JSON=false

while [ "$#" -gt 0 ]; do
  case $1 in
    --echo-json) ECHO_JSON=true ;;
    *) echo "Unknown parameter passed: $1"; exit 1 ;;
  esac
  shift
done

check_health() {
  echo "Checking health status..."
  response=$(curl -s -X GET "$BASE_URL/health")
  if echo "$response" | grep -q '"status": "healthy"'; then
    echo "Service is healthy."
  else
    echo "Health check failed."
    exit 1
  fi
}

fetch_affirmation() {
  echo "Fetching a random affirmation..."
  response=$(curl -s -X GET "$BASE_URL/fetch-affirmation")
  if echo "$response" | grep -q '"status": "success"'; then
    echo "Affirmation fetched successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Affirmation JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to fetch affirmation."
    exit 1
  fi
}

get_all_affirmations() {
  echo "Retrieving all stored affirmations..."
  response=$(curl -s -X GET "$BASE_URL/get-affirmations")
  if echo "$response" | grep -q '"status": "success"'; then
    echo "All affirmations retrieved successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Affirmations JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to retrieve affirmations."
    exit 1
  fi
}

clear_affirmations() {
  echo "Clearing all affirmations..."
  response=$(curl -s -X DELETE "$BASE_URL/clear-affirmations")
  if echo "$response" | grep -q '"status": "success"'; then
    echo "Affirmations cleared successfully."
  else
    echo "Failed to clear affirmations."
    exit 1
  fi
}

get_affirmation_count() {
  echo "Getting the count of affirmations..."
  response=$(curl -s -X GET "$BASE_URL/get-affirmation-count")
  if echo "$response" | grep -q '"status": "success"'; then
    echo "Affirmation count retrieved successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Count JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to get affirmation count."
    exit 1
  fi
}

create_user() {
  username=$1
  password=$2

  echo "Creating a new user: $username..."
  response=$(curl -s -X POST "$BASE_URL/create-user" \
    -H "Content-Type: application/json" \
    -d "{\"username\":\"$username\", \"password\":\"$password\"}")
  if echo "$response" | grep -q '"status": "success"'; then
    echo "User $username created successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to create user $username."
    echo "Response:"
    echo "$response" | jq .
    exit 1
  fi
}

login_user() {
  username=$1
  password=$2

  echo "Logging in as user: $username..."
  response=$(curl -s -X POST "$BASE_URL/login" \
    -H "Content-Type: application/json" \
    -d "{\"username\":\"$username\", \"password\":\"$password\"}")
  if echo "$response" | grep -q '"status": "success"'; then
    echo "User $username logged in successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to log in as user $username."
    echo "Response:"
    echo "$response" | jq .
    exit 1
  fi
}

update_password() {
  username=$1
  old_password=$2
  new_password=$3

  echo "Updating password for user: $username..."
  response=$(curl -s -X POST "$BASE_URL/update-password" \
    -H "Content-Type: application/json" \
    -d "{\"username\":\"$username\", \"old_password\":\"$old_password\", \"new_password\":\"$new_password\"}")
  if echo "$response" | grep -q '"status": "success"'; then
    echo "Password updated successfully for user $username."
    if [ "$ECHO_JSON" = true ]; then
      echo "Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to update password for user $username."
    echo "Response:"
    echo "$response" | jq .
    exit 1
  fi
}


check_health
clear_affirmations
fetch_affirmation
get_all_affirmations
get_affirmation_count

create_user "testuser" "password123"
login_user "testuser" "password123"
update_password "testuser" "password123" "newpassword456"
login_user "testuser" "newpassword456"



