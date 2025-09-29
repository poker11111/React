import React from 'react'
    
function List2(props) {

    const list = props.list
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

export default List2