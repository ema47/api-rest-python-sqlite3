
from flask import Flask, jsonify, request
import product_controller
from db import create_tables

app = Flask(__name__)


@app.route('/product', methods=["GET"])
def get_products():
    products = product_controller.get_products()
    return jsonify(products)


@app.route("/product", methods=["POST"])
def insert_product():
    product_details = request.get_json()
    name = product_details["name"]
    producType=product_details["producType"]
    price = product_details["price"]
    rating = product_details["rating"]
    image=product_details["image"]
    description=product_details["description"]
    result = product_controller.insert_product(name, producType, price, rating, image, description)
    return jsonify(result)

"""
@app.route("/product", methods=["PUT"])
def update_product():
    product_details = request.get_json()
    id = product_details["id"]
    name = product_details["name"]
    producType=product_details["producType"]
    price = product_details["price"]
    rating = product_details["rating"]
    image=product_details["image"]
    description=product_details["description"]
    result = product_controller.update_product(id, name, producType, price, rating, image, description)
    return jsonify(result)
"""

@app.route("/product/<id>", methods=["PUT"])
def update_product(id):
    product_details = request.get_json()
    """id = product_details["id"]"""
    name = product_details["name"]
    producType=product_details["producType"]
    price = product_details["price"]
    rating = product_details["rating"]
    image=product_details["image"]
    description=product_details["description"]
    result = product_controller.update_product(id, name, producType, price, rating, image, description)
    return jsonify(result)

@app.route("/product/<id>", methods=["DELETE"])
def delete_product(id):
    result = product_controller.delete_product(id)
    return jsonify(result)


@app.route("/product/<id>", methods=["GET"])
def get_product_by_id(id):
    product = product_controller.get_by_id(id)
    return jsonify(product)

"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)
