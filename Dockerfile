# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install python-dotenv 

# Install SQLite3
RUN apt-get update && apt-get install -y SQLAlchemy

# Define a volume for persisting the database
VOLUME ["/app/db"]

# Make port 5000 available to the world outside this container
EXPOSE 5001

# Run the entrypoint script when the container launches
CMD ["python", "app.py"]