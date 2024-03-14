FastAPI App in Docker Container
==============================

This repository contains a simple FastAPI app with train and predict endpoints, packaged in a Docker container for easy deployment.

Getting Started
---------------

1. Clone the repository to your local machine:
2. Go to `data_app` and run:
```bash
flask run --reload
```
3. Go to `model_app`
```bash
uvicorn app:app --reload
```
4. Go to `http://127.0.0.1:8000/docs` and check the app

Endpoints
---------

The model_app includes the following endpoints:

* **/train**: Trains a machine learning model
* **/predict**: Makes a prediction using the trained model (currently returns a random number)
  

The model_app includes the following endpoints:

* **/**: Adding new data
* **/add-row**: POST API for adding data to file
* **/get/data**: GET API for geting data in data.csv file.

App Code skeleton
--------

The main entry point for the app is `app.py`, which defines the train and predict endpoints:
```python
from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/train")
def train():
    # Train a machine learning model here
    return {"message": "Model trained successfully"}

@app.post("/predict")
def predict():
    # Make a prediction using the trained model here
    return {"prediction": round(random.random(), 2)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)
```
Dockerfile skeleton
----------

The `Dockerfile` builds the Docker image for the app:
```bash
# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
```

Task for classes
----------

Currently the ran can be tested localy without docker.
Your task is to:
- [ ] Create Dockerfile into model_app
- [ ] Create docker-compose.yaml in main folder `cw6`
- [ ] Specifuy volume in docker-compose so the data is persistent
- [ ] Run and test app