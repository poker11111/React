import React,{useState} from 'react'

export default function About() {

  const [name, setName] = useState("Dori")

  return (
    <>
    
    <h1>About Page</h1>
    <p>This is the About Page</p>

    <button onClick={() => setName("Profi")}>Change Name</button>
    <button onClick={() => setName("Dori")}>Reset Name</button>
    <p>{name}</p>
    </>
  )
}
