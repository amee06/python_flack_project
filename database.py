import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "flask_project"
)

print("Database connected successfully")
cursor = db.cursor()