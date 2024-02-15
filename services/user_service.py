from models.user import User
from flask_jwt_extended import create_access_token


roles = ["student", "teacher"]
def verifyDataUser(name, email, password):
    if name and email and password and "@" in email and "." in email and len(password) > 5 and len(name) > 5:
        return True
    else:
        return False



def create_user(name, email, password, role):
    if verifyDataUser(name, email, password) and role in roles:
        user = User(name=name, email=email, password=password, role=role)
        state = user.createUser()
        if state["mode"] == "success":
            jwt_token = create_access_token(identity=email)
            return {
                "mode": "success",
                "message": "User created successfully",
                "token": jwt_token
            }
        else: return state
    else:
        return {
            "mode": "error",
            "message": "Invalid data min length 6 for nameand password and valid email and role"
        }
    
def login_user(name, email, password):
    if verifyDataUser(name, email, password):
        user = User(name=name, email=email, password=password)
        state = user.login()
        if state["mode"] == "success":
            jwt_token = create_access_token(identity=email)
            return {
                "mode": "success",
                "message": "User logged in successfully",
                "token": jwt_token
            }
        else: return state
    else:
        return {
            "mode": "error",
            "message": "Invalid data min length 6 for nameand password and valid email and role"
        }

