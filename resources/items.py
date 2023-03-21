from flask import Blueprint, request, jsonify
from services.Services import Services
from repository.models.Item import Item

# Creating a blueprint

# A blueprint is a selection of common endpoints/routes to complete modularity to the flask applications

# Create the blueprint for the items, which will store all the endpoints related to the items itself.
items_bp = Blueprint("items", __name__)


@items_bp.route("/items/create-item", methods=["POST"])
def create_item():

    result = request.json

    if result and Item.is_correct_json(result) :
        result = Services.create_one(result)
        return jsonify({"Item created with id": result.inserted_id})
    else:
        return jsonify({"ERROR": "The item could not be inserted"})


@items_bp.route("/items/find-one/<id>", methods=["GET"])
def find_one(id):

    try:
        result = Services.read_one(int(id))
    except ValueError:
        return jsonify({"ERROR":"Item not found. Check the data and try again."})

    if result and Item.is_correct_json(result):
        return jsonify(result)
    else:
        return jsonify({"ERROR":"Item not found. Check the data and try again."})


@items_bp.route("/items/delete-one/<id>", methods=["DELETE"])
def delete_one(id):

    try:
        result = Services.delete_one(int(id))
    except ValueError:
        return jsonify({"ERROR":"Item not found. Check the data and try again."})
    
    if result and result.deleted_count==1:
        return jsonify({"Item id deleted": id})
    else:
        return jsonify({"ERROR":"Item not found. Check the data and try again."})


@items_bp.route("/items/update-one/<id>", methods=["PUT"])
def update_one(id):

    result = None
    if Item.correct_update_statement(request.json):
        result = Services.update_one(int(id), request.json)

    if result and result.modified_count == 1:
        return jsonify({"Item id updated": id})
    else:
        return jsonify({"ERROR":"Please, update action not posible. Check the data and try again"})
