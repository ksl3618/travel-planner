import React from 'react'
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Wishlist from './Wishlist'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h1>Wishlist</h1>
      <Wishlist />
    </>
  )
}

export default App
