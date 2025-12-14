from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Connect to RDS MySQL
db = mysql.connector.connect(
    host="database-1.cuvc0q68a5fv.us-east-1.rds.amazonaws.com",  # Replace with your RDS endpoint
    user="admin",         # Your RDS username
    password="Selvamani#1",  # Your RDS password
    database="mydatabase"     # Your database name
)

@app.route("/users")
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

if __name__ == "__main__":
    # Run app on all interfaces, port 5000
    app.run(host="0.0.0.0", port=5000)
