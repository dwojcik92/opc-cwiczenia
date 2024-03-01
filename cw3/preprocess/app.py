from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    'host': 'db',          # Service name in Docker Compose network
    'user': 'my_user',
    'password': 'my_password',
    'database': 'train_database'
}

# Function to fetch data from the database
def get_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM trains')
        data = cursor.fetchall()
        print(data)
        return data
    except mysql.connector.Error as error:
        return f"Error: {error}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/')
def index():
    # Fetch data from the database
    data = get_data()
    data_json = {
        "data": data
    }
    return jsonify(message="Preprocess received response from Database",
                   database_response=data_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)