from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://train:5000')
    return jsonify(message="App received response from Train",
                   train_response=response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
