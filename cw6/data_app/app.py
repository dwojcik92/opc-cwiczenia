import os
import csv
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
data_file = 'data.csv'

@app.route('/')
def index():
    if not os.path.exists(data_file):
        with open(data_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['X', 'Y'])
    return render_template('index.html', table=pd.read_csv(data_file))

@app.route('/add-row', methods=['POST'])
def add_row():
    new_row = {key: value for key, value in request.form.items()}
    with open(data_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_row.values())
    return redirect(url_for('index'))

@app.route("/get/data")
def get_data():
    dataframe = pd.read_csv(data_file)
    data = dataframe.to_numpy().tolist()
    print(data)
    return jsonify(data=data)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')