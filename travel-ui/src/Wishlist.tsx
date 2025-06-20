import { useState, useEffect } from 'react';
import './Wishlist.css';

function Wishlist() {
  const [wishlist, setWishlist] = useState([]);
  const [destination, setDestination] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/wishlist')
      .then(res => res.json())
      .then(data => setWishlist(data));
  }, []);

  const addDestination = () => {
    fetch('http://localhost:5000/api/wishlist', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ destination }),
    })
      .then(res => res.json())
      .then(data => setWishlist(data.wishlist));
    setDestination('');
  };

  return (
    <div>
      <div className="input-row">
        <input
          value={destination}
          onChange={e => setDestination(e.target.value)}
          placeholder="Add destination"
        />
        <button onClick={addDestination}>Add</button>
      </div>
      <ul>
        {wishlist.map((place, idx) => <li key={idx}>{place}</li>)}
      </ul>
    </div>
  );
}

export default Wishlist;
