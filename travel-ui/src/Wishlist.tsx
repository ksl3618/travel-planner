import { useState, useEffect } from 'react';
import './Wishlist.css';

type Location = {
  name: string;
  destinations: string[];
};

function Wishlist() {
  const [wishlist, setWishlist] = useState<Location[]>([]);
  const [destination, setDestination] = useState('');
  const [locationName, setLocationName] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/wishlist')
      .then(res => res.json())
      .then(data => setWishlist(data));
  }, []);

  const addLocation = () => {
    if (!locationName.trim() || !destination.trim()) return;
    fetch('http://localhost:5000/api/wishlist', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: locationName, destinations: [destination] }),
    })
      .then(res => res.json())
      .then(data => setWishlist(data.wishlist));
    setLocationName('');
    setDestination('');
  };

  const addDestination = (locationName: string) => {
    fetch(`http://localhost:5000/api/wishlist/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: locationName, destinations: [destination] }),
    })
      .then(res => res.json())
      .then(data => setWishlist(data.wishlist));
    setDestination('');
    setLocationName('');
  }

  return (
    <div>
      <div className="input-row">
        <input
          value={locationName}
          onChange={e => setLocationName(e.target.value)}
          placeholder="Add location"
        />
        <input
          value={destination}
          onChange={e => setDestination(e.target.value)}
          placeholder="Add destination"
        />
        <button onClick={addLocation}>Add</button>
      </div>
      <ul>
        {wishlist.map((loc, idx) => (
          <li key={idx}>
            <strong>{loc.name}</strong>
            <ul>
              {loc.destinations.map((dest, idx) => <li key={idx}>{dest}</li>)}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Wishlist;
