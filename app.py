from flask import Flask
from routes import users_routes

app = Flask(__name__)

app.register_blueprint(users_routes.bp)



if __name__ == "__main__":
    app.run(debug=True, port=5000)