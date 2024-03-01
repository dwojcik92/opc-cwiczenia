# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask

# Set environment variables
ENV FLASK_APP=app2.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5002
EXPOSE 5002

# Run the Flask application
CMD ["python", "app2.py"]
