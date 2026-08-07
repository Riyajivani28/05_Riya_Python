from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample Data for Task 2 (Flipkart Wishlist)
wishlist_products = [
    {
        "id": 101,
        "name": "Apple iPhone 15 Pro (128 GB)",
        "price": "₹1,27,990"
    },
    {
        "id": 102,
        "name": "Sony WH-1000XM5 Wireless Headphones",
        "price": "₹28,990"
    },
    {
        "id": 103,
        "name": "Nike Air Max 270 Sneakers",
        "price": "₹12,495"
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=wishlist_products)

# API Endpoint for Task 2: Flipkart Wishlist Delete
@app.route('/api/wishlist/<int:product_id>', methods=['DELETE'])
def remove_from_wishlist(product_id):
    global wishlist_products
    initial_length = len(wishlist_products)
    wishlist_products = [p for p in wishlist_products if p['id'] != product_id]
    
    if len(wishlist_products) < initial_length:
        return jsonify({"success": True, "message": f"Product {product_id} removed from wishlist."}), 200
    else:
        return jsonify({"success": False, "message": "Product not found."}), 404

# API Endpoint for Task 3: BookMyShow Movie Delete (JSON payload)
@app.route('/api/watchlater/<int:movie_id>', methods=['DELETE'])
def remove_from_watchlater(movie_id):
    data = request.get_json(silent=True) or {}
    movie_title = data.get('title', 'Movie')
    return jsonify({
        "success": True,
        "message": f'"{movie_title}" successfully removed from your Watch Later list!'
    }), 200

# API Endpoint for Task 1 & Task 4: Dummy Playlist / Song Delete Endpoint
@app.route('/api/delete-item/<int:item_id>', methods=['DELETE'])
def delete_generic_item(item_id):
    return jsonify({"success": True, "message": f"Item {item_id} deleted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
