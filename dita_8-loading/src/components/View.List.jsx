import React from 'react'

function View() {
  return (
    <>

          <div key={item.id}>
            <h2>{item.name}</h2>  
            <p>Age: {item.age}</p>
            <p>City: {item.city}</p>
            
            
            <button onClick={() => deleteButton(item.id)}>Hide</button>
          </div>
      
    </>
  )
}

export default View