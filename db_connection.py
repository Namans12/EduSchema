
import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="naman1201",
        database="EduSchema"
    )
    return connection
