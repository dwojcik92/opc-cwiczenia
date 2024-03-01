from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://app2:5002')
    return jsonify(message="App1 received response from App2",
                   app2_response=response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
