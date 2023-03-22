from flask import Blueprint, jsonify
from services.Services import Services
from repository.models.Item import Item
from repository.models.check_item import correct_update_statement


# Creating a blueprint

# A blueprint is a selection of common endpoints/routes to complete modularity to the flask applications

# Create the blueprint for the items, which will store all the endpoints related to the items itself.
inventory_bp = Blueprint("inventory", __name__)


@inventory_bp.route("/inventory", methods=["GET"])
def get_inventory():
    inventory = Services.inventory()
    return jsonify(inventory)


@inventory_bp.route("/inventory/update", methods=["PUT"])
def update_inventory():
    inventory = Services.inventory()

    for item in inventory:
        item_to_object = Item(
            item["_id"],
            item["name"],
            item["sell_in"],
            item["quality"],
            item["item_type"],
        )

        if correct_update_statement(item_to_object.update_statement()):
            Services.update_one(item["_id"], item_to_object.update_statement())

    inventory = Services.inventory()

    return jsonify(inventory)
