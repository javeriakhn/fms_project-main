import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="AlexLee1163957.mysql.pythonanywhere-services.com",  # MySQL host
        user="AlexLee1163957",  # Your PythonAnywhere username
        password="dltjdals@1025",  # The password you set for MySQL
        database="AlexLee1163957$fmsproject"  # Full database name
    )
    return connection
