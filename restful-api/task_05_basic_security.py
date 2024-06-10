#!/usr/bin/python3
"""Module for secure API"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt_claims
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'  # Change this to a strong secret key in production
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# User data stored in memory
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpassword"), "role": "admin"}
}

# Basic Authentication
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username

# JWT Authentication
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username, user_claims={"role": user['role']})
    return jsonify(access_token=access_token), 200

# JWT Protected Route
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(message="JWT Auth: Access Granted for {}".format(current_user)), 200

# Role-based Protected Route
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    user_role = get_jwt_claims()['role']
    if user_role != 'admin':
        return jsonify({"error": "Forbidden"}), 403
    return jsonify(message="Admin Access: Granted for {}".format(current_user)), 200

# Basic Authentication Protected Route
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted"), 200

# Custom Error Handlers for JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run(debug=True)

