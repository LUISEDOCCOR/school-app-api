from models.user import User

roles = ["student", "teacher"]
def verifyDataUser(name, email, password):
    if name and email and password and "@" in email and "." in email and len(password) > 5 and len(name) > 5:
        return True
    else:
        return False



def create_user(name, email, password, role):
    if verifyDataUser(name, email, password) and role in roles:
        user = User(name=name, email=email, password=password, role=role)
        return user.createUser()
    else:
        return {
            "mode": "error",
            "message": "Invalid data min length 6 for nameand password and valid email and role"
        }
    
def login_user(name, email, password):
    if verifyDataUser(name, email, password):
        user = User(name=name, email=email, password=password)
        return user.login()
    else:
        return {
            "mode": "error",
            "message": "Invalid data min length 6 for nameand password and valid email and role"
        }

