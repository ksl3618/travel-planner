from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from typing import List, Optional

WISHLIST_FILE = 'wishlist.json'

app = Flask(__name__)
CORS(app)

''' --------------Model---------------- '''
#Location object to store locations and destinations at each location.
class Location:
    def __init__(self, name: str, destinations: Optional[List[str]] = None):
        self.name = name
        self.destinations = destinations if destinations is not None else []

    def get_name(self) -> str:
        return self.name

    def get_destinations(self) -> List[str]:
        return self.destinations

    def add_destination(self, destination: str):
        self.destinations.append(destination)

    def to_dict(self):
        return {'name': self.name, 'destinations': self.destinations}

    @staticmethod
    def from_dict(data):
        return Location(name=data['name'], destinations=data.get('destinations', []))


''' --------------Controller---------------- '''
def load_wishlist():
    if not os.path.exists(WISHLIST_FILE):
        return []
    with open(WISHLIST_FILE, 'r') as f:
        data = json.load(f)
        return [Location.from_dict(item) for item in data]

def save_wishlist(wishlist: List[Location]):
    with open(WISHLIST_FILE, 'w') as f:
        json.dump([loc.to_dict() for loc in wishlist], f)

#Get all locations
@app.route('/api/wishlist', methods=['GET'])
def get_wishlist():
    wishlist = load_wishlist()
    return jsonify([loc.to_dict() for loc in wishlist])

#Get a specific location
@app.route('/api/wishlist/<string:name>', methods=['GET'])
def get_location(name: str):
    wishlist = load_wishlist()
    for loc in wishlist:
        if loc.name == name:
            return jsonify(loc.to_dict())
    return jsonify({'error': 'Location not found'}), 404

#Add a new location
@app.route('/api/wishlist', methods=['POST'])
def add_location():
    data = request.get_json()
    name = data.get('name')
    destinations = data.get('destinations', [])
    if name:
        wishlist = load_wishlist()
        # Check if location already exists
        for loc in wishlist:
            if loc.name == name:
                # Optionally, merge destinations if provided
                for dest in destinations:
                    if dest not in loc.destinations:
                        loc.add_destination(dest)
                save_wishlist(wishlist)
                return jsonify({'message': 'Updated!', 'wishlist': [l.to_dict() for l in wishlist]}), 200
        # If not found, add new location
        new_location = Location(name=name, destinations=destinations)
        wishlist.append(new_location)
        save_wishlist(wishlist)
        return jsonify({'message': 'Added!', 'wishlist': [l.to_dict() for l in wishlist]}), 201
    return jsonify({'error': 'No location name provided'}), 400

if __name__ == '__main__':
    app.run(port=5000)
