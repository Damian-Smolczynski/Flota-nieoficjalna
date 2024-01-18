import React from "react"
import { Routes, Route } from 'react-router-dom';
import CarsRestAPI from "./CarsRestAPI";



const App = () =>  {
    return (
        <Routes>
            <Route path="/" element={(<CarsRestAPI/>)}/>
        </Routes>
    )

}

export default App