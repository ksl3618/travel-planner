from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

wishlist = []

@app.route('/api/wishlist', methods=['GET'])
def get_wishlist():
    return jsonify(wishlist)

@app.route('/api/wishlist', methods=['POST'])
def add_wishlist():
    data = request.get_json()
    destination = data.get('destination')
    if destination:
        wishlist.append(destination)
        return jsonify({'message': 'Added!', 'wishlist': wishlist}), 201
    return jsonify({'error': 'No destination provided'}), 400

if __name__ == '__main__':
    app.run(port=5000)
