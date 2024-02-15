from models.db import database
import bcrypt

class User(database):
    def __init__(self, name=None, email=None, password=None, role=None, id=None):
        super().__init__()
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.id = id

    def existUser(self):
        query = "SELECT * FROM users WHERE email=%s and name=%s"
        self.cursor.execute(query, (self.email, self.name))
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False

    def createUser(self):
        if not self.existUser():

            self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())

            query = "INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (self.name, self.email, self.password, self.role))
            self.conn.commit()
            return {
                "mode": "success",
                "message": "User created successfully"
            }
        else:
            return {
                "mode": "error",
                "message": "User already exists"
            }
        
    def login(self):
        query = "SELECT * FROM users WHERE email=%s and name=%s"
        self.cursor.execute(query, (self.email, self.name))
        result = self.cursor.fetchall()
        if result:
            if bcrypt.checkpw(self.password.encode('utf-8'), result[0][3].encode('utf-8')):
                return {
                    "mode": "success",
                    "message": "User logged in successfully"
                }
            else:
                return {
                    "mode": "error",
                    "message": "Invalid password"
                }
        else: return{
            "mode": "error",
            "message": "User does not exist"
        
        }


