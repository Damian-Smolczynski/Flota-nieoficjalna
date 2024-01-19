import React from "react"
import { Routes, Route } from 'react-router-dom';
import CarsRestAPI from "./CarsRestAPI";
import LoginForm from "./LoginForm";
import Register from "./Register";
import WidokPojazdow from "./components/WidokPojazdow";



const App = () =>  {
    return (
        <Routes>
            <Route path="/" element={(<CarsRestAPI/>)}/>
            <Route path="/login" element={(<LoginForm/>)}/>
            <Route path="/register" element={(<Register/>)}/>
            <Route path='/widok-pojazdow' element={WidokPojazdow}/>
        </Routes>
    )

}

export default App