import mysql.connector

db_config = {
    "host":"localhost",
    "user":"root",
    "password": "",
    "database": "school-app"
}


class database:
    def __init__(self):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()
    