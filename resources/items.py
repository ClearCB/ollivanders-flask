from flask import Blueprint, request, jsonify
from services.Services import Services

# Creating a blueprint

# A blueprint is a selection of common endpoints/routes to complete modularity to the flask applications

# Create the blueprint for the items, which will store all the endpoints related to the items itself. 
items_bp = Blueprint("items", __name__)

@items_bp.route("/items/create-item", methods=["POST"])
def create_item():
    item = request.json
    result = Services.create_one(item)
    return jsonify({"_id": result.inserted_id})

@items_bp.route("/items/find-one/<id>", methods=["GET"])
def find_one(id):
    item = Services.read_one(int(id))
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"})
    
@items_bp.route("/items/delete-one/<id>", methods=["DELETE"])
def delete_one(id):

    item = Services.delete_one(int(id))
    if item:
        return jsonify(id)
    else:
        return jsonify({"error": "Item not found"})
    