from fastapi import FastAPI, UploadFile, File
import uvicorn
import requests
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from PIL import Image
from pydantic import BaseModel
from typing import List
import io

app = FastAPI()

class InputData(BaseModel):
    data: List[float]

# Define a simple neural network model using scikit-learn
model = MLPClassifier(hidden_layer_sizes=(100,), random_state=42)

@app.post("/train")
def train():
    
    req = requests.get("http://0.0.0.0:5000/get/data")
    data = req.json()
    data = data["data"]
    data = np.array(data)
    print(data.shape)
    X = data[:,0].reshape(-1, 1)
    y = data[:,1].reshape(-1, 1)
    
    print(data)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # Train the model on the updated training set
    model.fit(X_train, y_train)
    
    return {"message": "Model trained successfully"}

@app.post("/predict")
def predict(input_data: InputData):
    data = np.array(input_data.data).reshape(1, -1)
    # Make a prediction on the new image
    y_pred = model.predict(data)
    
    return {"prediction": int(y_pred[0])}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)