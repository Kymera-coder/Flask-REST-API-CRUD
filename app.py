from flask import Flask, jsonify, request

app = Flask(__name__)

# Simula um banco de dados
items = []

@app.route("/")
def home():
    return jsonify({"message": "Flask REST API is running"})

# CREATE
@app.route("/items", methods=["POST"])
def create_item():
    data = request.json
    items.append(data)
    return jsonify({"message": "Item added", "item": data}), 201

# READ
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# UPDATE
@app.route("/items/<int:index>", methods=["PUT"])
def update_item(index):
    if index < len(items):
        items[index] = request.json
        return jsonify({"message": "Item updated", "item": items[index]})
    return jsonify({"error": "Item not found"}), 404

# DELETE
@app.route("/items/<int:index>", methods=["DELETE"])
def delete_item(index):
    if index < len(items):
        removed = items.pop(index)
        return jsonify({"message": "Item deleted", "item": removed})
    return jsonify({"error": "Item not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
