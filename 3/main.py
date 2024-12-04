def organizeInventory(inventory: list):
    # Code here
    result = {}
    for item in inventory:
        category = item["category"]
        name = item["name"]
        quantity = item["quantity"]
        if category not in result:
            result[category] = {}
        if name not in result[category]:
            result[category][name] = 0
        result[category][name] += quantity

    return result


if __name__ == "__main__":
    inventory = [
        {"name": "doll", "quantity": 5, "category": "toys"},
        {"name": "car", "quantity": 3, "category": "toys"},
        {"name": "ball", "quantity": 2, "category": "sports"},
        {"name": "car", "quantity": 2, "category": "toys"},
        {"name": "racket", "quantity": 4, "category": "sports"},
    ]

    print(organizeInventory(inventory))
