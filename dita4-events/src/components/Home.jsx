import React from 'react'
import Button from './Button.jsx'

function Home() {

  const para = {
    backgroundColor : "blue",
    fontSize: 20
  }

  const h2 = {
    backgroundColor : "red",
    fontSize: 20
  }

  return (
    <>
    <div>Home</div>
    <h1 style={{color: "red", fontSize: 20}}>Home Page</h1>
    <h2 style={h2}>Welcome</h2>
    <p style={para}>Welcome to the Home Page</p>
    <Button />
    </>
  )
}

export default Home
