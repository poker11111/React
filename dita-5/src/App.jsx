import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from './components/Home.jsx'
import Navbar from './components/Navbar.jsx'
import Button from  './components/Button.jsx'
import About from './components/About.jsx'
import Contact from './components/Contact.jsx'

function App() {


  return (
    <>
      <div>
        <Navbar />
      </div>

      <div>
         <Home />
      </div>

    
    </>
  )
}

export default App
