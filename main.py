from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Headphones", "price": 49.99},
    {"id": 3, "name": "Keyboard", "price": 29.99},
]

cart = []


@app.route("/")
def home():
    return jsonify({"message": "Welcome to Broken Simple Shop API"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)


@app.route("/cart", methods=["GET"])
def get_cart():
    return jsonify(cart)


@app.route("/cart/add", methods=["POST"])
def add_to_cart():
    data = request.get_json(silent=True)
    if not data or "product_id" not in data:
        return jsonify({"error": "product_id is required"}), 400
    product = next(
        (p for p in products if p["id"] == data["product_id"]), None
    )
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    cart.append(product)
    return jsonify({"message": "Added to cart", "cart": cart}), 201


if __name__ == "__main__":
    # 0.0.0.0 is required so the container is reachable from outside
    app.run(host="0.0.0.0", port=5000)  # nosec B104
