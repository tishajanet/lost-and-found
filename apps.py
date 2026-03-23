from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MysqlTisha2026",
    database="lost_and_found"
)

@app.route("/items")
def get_items():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    return jsonify(items)


if __name__ == "__main__":
    app.run(debug=True)