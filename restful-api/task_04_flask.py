#!/usr/bin/python3
"""Module containing simple Flask web application"""

from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

users = {}


@api.route('/')
class Home(Resource):
    def get(self):
        return 'Welcome to the Flask API!'


@api.route('/data')
class Data(Resource):
    def get(self):
        return jsonify(list(users))


user_model = api.model('User', {
    'username': fields.String(required=True),
    'name': fields.String(),
    'age': fields.Integer(),
    'city': fields.String()
})


@api.route('/add_user')
class AddUser(Resource):
    @api.expect(user_model)
    def post(self):
        data = request.json
        if data is None or data.get('username') is None:
            return jsonify({'error': 'Username is required'}), 400
        user = {
            'username': data.get('username'),
            'name': data.get('name'),
            'age': data.get('age'),
            'city': data.get('city')
        }
        users[user.get('username')] = user
        return jsonify({'message': 'User added', 'user': user}), 201


@api.route('/status')
class Status(Resource):
    def get(self):
        return 'OK'


@api.route('/users/<username>')
class Username(Resource):
    def get(self, username):
        if username is None:
            return jsonify({'error': 'Username is required'}), 400
        if username not in users:
            return jsonify({"error": "User not found"}), 404
        return jsonify(users[username])


if __name__ == "__main__":
    app.run()

