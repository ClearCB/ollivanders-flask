# Posible item types
correct_item_type = ["Sulfuras", "NormalItem", "Conjured", "Backstage", "AgedBrie"]
# Keys that an item MUST have
correct_keys = ["_id", "sell_in", "quality", "item_type", "name"]
# Data type that must be int
int_values = ["sell_in", "quality"]


# Check if an item is correct as the database model in mongo
def is_correct_json(item):
    # The json must have 5 values
    if len(item) != len(correct_keys):
        return False

    for key in item:
        # Check if keys are correct
        if key not in correct_keys:
            return False

        # Check if the values are correct type
        elif key in int_values:
            try:
                int(item[key])
            except ValueError:
                return False

        # Check if the item type is correct
        elif key == "item_type" and item[key] not in correct_item_type:
            return False

    return True


# Check if the update statement is correct to update and item in mongo
def correct_update_statement(update_statement):
    for key in update_statement:
        # Check if keys are correct
        if key == "_id" or key == "item_type":
            return False

        # Check if the values are correct type
        elif key in int_values:
            try:
                int(update_statement[key])
            except ValueError:
                return False

    return True
