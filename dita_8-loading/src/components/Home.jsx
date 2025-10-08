import React, { useState, useEffect } from 'react'
import BlogList from './BlogList.jsx'
import './Home.css'

function Home() {
    const [list, setList] = useState([])
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(true)

        useEffect(() => {
         fetch('http://localhost:823/list')
         .then(res => {
              return res.json()
         })

         .then(data => {
              setList(data)
              setLoading(false)
         })
         
         .catch(err => {
          setError("Could not fetch data")
          setLoading(false)
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
       { loading && <div><img src={myImage} alt="" /></div> }
       { error && <div>{ error }</div> } 

        {list && <BlogList  list={list} x = "Lista e Nxenesve" deleteButton={deleteButton} /> }
    </>
  )
}

export default Home