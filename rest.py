from flask import Flask, request, jsonify

from data import update_data, data

app = Flask(__name__)
update_data()


@app.get("/")
def get_categories():
    categories = []
    for category in data:
        categories.append(category)
    return jsonify(categories)


@app.get("/<category>")
def get_items(category):
    if category in data:
        items = []
        for item in data[category]:
            items.append(item)
        return jsonify(items)
    else:
        return "Category doesn't exist."


@app.get("/<category>/<character_name>")
def get_data(category, character_name):
    if category in data and character_name in data[category]:
        return jsonify(data[category][character_name])
    else:
        return "Data doesn't exist."

