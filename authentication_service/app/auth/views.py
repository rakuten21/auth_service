from flask import Blueprint, request, jsonify
from app.models import create_user, get_user_by_username
from app.utils import hash_password, check_password_hash
from .tokens import generate_token, decode_token

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    
    existing_user = get_user_by_username(username)
    if existing_user:
        return jsonify({'message': 'User already exists'}), 409
    
    password_hash = hash_password(password)
    create_user(username, password_hash)

    return jsonify({'message': 'User created successfully'}), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400

    user = get_user_by_username(username)
    if user and check_password_hash(password, user[2]):
        token = generate_token(user[0])
        return jsonify({'token': token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    # This endpoint informs the client to remove the token
    return jsonify({'message': 'Logout successful'}), 200
