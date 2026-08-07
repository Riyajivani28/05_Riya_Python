from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample Wishlist Products Data
wishlist_products = [
    {
        "id": 101,
        "name": "Apple iPhone 15 Pro (128 GB) - Natural Titanium",
        "price": "₹1,27,990",
        "image": "https://via.placeholder.com/120?text=iPhone+15"
    },
    {
        "id": 102,
        "name": "Sony WH-1000XM5 Wireless Headphones",
        "price": "₹28,990",
        "image": "https://via.placeholder.com/120?text=Sony+Headphones"
    },
    {
        "id": 103,
        "name": "Nike Air Max 270 Sneakers",
        "price": "₹12,495",
        "image": "https://via.placeholder.com/120?text=Nike+Shoes"
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=wishlist_products)

# API Endpoint to handle AJAX DELETE Request
@app.route('/api/wishlist/<int:product_id>', methods=['DELETE'])
def remove_from_wishlist(product_id):
    global wishlist_products
    # Find product and remove from backend data store
    initial_length = len(wishlist_products)
    wishlist_products = [p for p in wishlist_products if p['id'] != product_id]
    
    if len(wishlist_products) < initial_length:
        return jsonify({"success": True, "message": f"Product {product_id} removed from wishlist."}), 200
    else:
        return jsonify({"success": False, "message": "Product not found."}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
