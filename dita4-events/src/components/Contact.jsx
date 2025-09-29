import React, {useState} from 'react'

export default function Contact() {
  
    const [list, setList] = useState([
    {id: 1, name: "Dori", age: 15, city: "Prizren" },
    {id: 2, name: "Profi", age: 31, city: "Prishtine" },
    {id: 3, name: "Lori", age: 25, city: "Peje" },
    {id: 4, name: "Bori", age: 29, city: "Prizren" },
    {id: 5, name: "Tori", age: 19, city: "Prishtine" },
  ])

  return (
    <>
        <h1>Contact</h1>
      <p>This is the Contact Page</p>

      {list.map((item) => (
        <div key={item.id}>
          <h2>{item.name}</h2>
          <p>Age: {item.age}</p>
          <p>City: {item.city}</p>
        </div>
      ))}
    </>
  )
}
