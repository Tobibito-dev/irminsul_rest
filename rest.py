from flask import Flask, request, jsonify

from data import update_data, data

app = Flask(__name__)
update_data()
app.run()


@app.get("/genshin")
def get_countries():
    print(data)
    return jsonify(data)


@app.post("/genshin")
def add_countries():
    if request.is_json:
        country = request.get_json()
        country['id'] = 100
        data.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415
