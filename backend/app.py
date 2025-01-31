from flask import Flask, jsonify

app = Flask(__name__)

inventory = [
    {"id": 1, "name": "Item A", "quantity": 100},
    {"id": 2, "name": "Item B", "quantity": 200},
]

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

if __name__ == '__main__':
    app.run(debug=True)