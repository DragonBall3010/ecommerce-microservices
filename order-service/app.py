from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({"orders": [
        {"id": 1, "user": "Alice", "product": "Laptop", "quantity": 1, "status": "Delivered"},
        {"id": 2, "user": "Bob", "product": "Smartphone", "quantity": 2, "status": "Shipped"},
        {"id": 3, "user": "Charlie", "product": "Headphones", "quantity": 1, "status": "Processing"}
    ]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
