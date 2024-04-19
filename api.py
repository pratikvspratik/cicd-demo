from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

items = []

@api.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@api.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    items.append(data)
    return jsonify(data), 205

@api.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    data = request.get_json()
    items[index] = data
    return jsonify(data)

@api.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    del items[index]
    return '', 204