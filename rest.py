from flask import Flask, request, jsonify

from data import update_data, data

app = Flask(__name__)
update_data()


# names
@app.get("/")
def get_categories():
    categories = []
    for category in data:
        categories.append(category)
    return jsonify(categories)


@app.get("/<category>")
def get_item_names(category):
    if category in data:
        items = []
        for item in data[category]:
            items.append(item)
        return jsonify(items)
    else:
        return "Category doesn't exist."


@app.get("/<category>/<item_name>")
def get_item_name(category, item_name):
    if category in data and item_name in data[category]:
        return jsonify(data[category][item_name]['name'])
    else:
        return "Item doesn't exist."


# data
@app.get("/data")
def get_all_data():
    return data


@app.get("/<category>/data")
def get_category_data(category):
    if category in data:
        return data[category]
    else:
        return "Category doesn't exist"

@app.get("/<category>/<item_name>/data")
def get_item_data(category, item_name):
    if category in data and item_name in data[category]:
        return jsonify(data[category][item_name])
    else:
        return "Item doesn't exist."



