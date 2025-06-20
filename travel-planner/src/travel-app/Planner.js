/**
 * Planner.js
 * This file contains the main application component for the travel planner.
 * It imports the Wishlist component and renders it within the main application.
 */

import React from 'react';
import Wishlist from './components/Wishlist';

function App() {
  return (
    <div>
      <h1>Travel Planner</h1>
      <Wishlist />
    </div>
  );
}

export default App;