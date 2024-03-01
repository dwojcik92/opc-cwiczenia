# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask requests

# Set environment variables
ENV FLASK_APP=app1.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5001
EXPOSE 5001

# Run the Flask application
CMD ["python", "app1.py"]
