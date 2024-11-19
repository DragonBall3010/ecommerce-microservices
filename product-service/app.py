from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": [
        {"id": 1, "name": "Laptop", "price": 1000},
        {"id": 2, "name": "Smartphone", "price": 800},
        {"id": 3, "name": "Headphones", "price": 200}
    ]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
