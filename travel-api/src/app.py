from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

WISHLIST_FILE = 'wishlist.json'

app = Flask(__name__)
CORS(app)

def load_wishlist():
    if not os.path.exists(WISHLIST_FILE):
        return []
    with open(WISHLIST_FILE, 'r') as f:
        return json.load(f)

def save_wishlist(wishlist):
    with open(WISHLIST_FILE, 'w') as f:
        json.dump(wishlist, f)

@app.route('/api/wishlist', methods=['GET'])
def get_wishlist():
    wishlist = load_wishlist()
    return jsonify(wishlist)

@app.route('/api/wishlist', methods=['POST'])
def add_wishlist():
    data = request.get_json()
    destination = data.get('destination')
    if destination:
        wishlist = load_wishlist()
        wishlist.append(destination)
        save_wishlist(wishlist)
        return jsonify({'message': 'Added!', 'wishlist': wishlist}), 201
    return jsonify({'error': 'No destination provided'}), 400

if __name__ == '__main__':
    app.run(port=5000)
