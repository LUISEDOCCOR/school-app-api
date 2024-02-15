from flask import Flask
from routes import users_routes
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

app.register_blueprint(users_routes.bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)