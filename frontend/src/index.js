import React from 'react';
import ReactDOM from 'react-dom/client';
import App from "./App";
import CarsRestAPI from "./CarsRestAPI";
import {BrowserRouter} from "react-router-dom";
// import "./stylesheets/Main.css"
import WidokPojazdow from "./stylesheets/WidokPojazdow";
import "./stylesheets/WidokPojazdow.css"


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      {/*<BrowserRouter>*/}
      {/*    <App/>*/}
      {/*</BrowserRouter>*/}
      <WidokPojazdow/>
  </React.StrictMode>
);

