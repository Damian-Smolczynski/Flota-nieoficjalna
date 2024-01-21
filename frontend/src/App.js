import React from "react"
import { Routes, Route } from 'react-router-dom';
import CarsRestAPI from "./CarsRestAPI";
import LoginForm from "./components/authorisation/LoginForm";
import Register from "./components/authorisation/Register";
import CarsView from "./components/CarsView";



const App = () =>  {
    return (
        <Routes>
            <Route path="/" element={(<CarsRestAPI/>)}/>
            <Route path="/login" element={(<LoginForm/>)}/>
            <Route path="/register" element={(<Register/>)}/>
            <Route path='/widok-pojazdow' element={CarsView}/>
        </Routes>
    )

}

export default App