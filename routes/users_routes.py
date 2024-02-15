from flask import Blueprint, request, jsonify
import services.user_service as user_service 


bp = Blueprint('users', __name__, url_prefix='/user')


@bp.route('/create', methods=['POST'])
def create_user():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        role = request.json['role']
        return jsonify(user_service.create_user(name=name, email=email, password=password, role=role))
    except:
        return jsonify({
            "mode": "error",
            "message": "Invalid request"
        })

@bp.route('/login', methods=['POST'])
def login():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        return jsonify(user_service.login_user(name=name, email=email, password=password))
    except:
        return jsonify({
            "mode": "error",
            "message": "Invalid request"
        })
    
