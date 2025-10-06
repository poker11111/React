import React, { useState, useEffect } from 'react'
import BlogList from './BlogList.jsx'

function Home() {
    const [list, setList] = useState([])

        useEffect(() => {
         fetch('http://localhost:3000/list')
         .then(res => {
              return res.json()
         })

         .then(data => {
              setList(data)
         })
         
         .catch(err => {
          console.log(err.message);
         }

         )
        }
      )

      const deleteButton = (id) => {
        const newList = list.filter(list => list.id !== id);

        setList(newList);
      }
  return (
    <>
        {/* {list.map((item) => (
          <div key={item.id}>
            <h2>{item.name}</h2>  
            <p>Age: {item.age}</p>
            <p>City: {item.city}</p>
          </div>
        ))} */}
        <BlogList  list={list} x = "Lista e Nxenesve" deleteButton={deleteButton} />
    </>
  )
}

export default Home