from flask import Blueprint, request, jsonify
from services.Services import Services
from repository.models.Item import Item

message_error = "Item not found"

# Creating a blueprint

# A blueprint is a selection of common endpoints/routes to complete modularity to the flask applications

# Create the blueprint for the items, which will store all the endpoints related to the items itself.
items_bp = Blueprint("items", __name__)


@items_bp.route("/items/create-item", methods=["POST"])
def create_item():

    item = request.json

    if Item.is_correct(item):
        result = Services.create_one(item)
        return {"_id": result.inserted_id}
    else:
        return {"ERROR": "The item could not be inserted"}


@items_bp.route("/items/find-one/<id>", methods=["GET"])
def find_one(id):

    try:
        result = Services.read_one(int(id))
    except ValueError:
        return {"ERROR":"Item not found. Check the data and try again."}

    if Item.is_correct(result.json):
        return result
    else:
        return {"ERROR":"Item not found. Check the data and try again."}


@items_bp.route("/items/delete-one/<id>", methods=["DELETE"])
def delete_one(id):

    try:
        result = Services.delete_one(int(id))
    except ValueError:
        return {"ERROR":"Item not found. Check the data and try again."}
    
    if result.deleted_count==1:
        return jsonify({"Item id deleted": id})
    else:
        return {"ERROR":"Item not found. Check the data and try again."}


@items_bp.route("/items/update-one/<id>", methods=["PUT"])
def update_one(id):

    result = Services.update_one(int(id), request.json)
    if result != error:
        return jsonify({"Item id updated": id})
    else:
        return jsonify({"ERROR": message_error})
