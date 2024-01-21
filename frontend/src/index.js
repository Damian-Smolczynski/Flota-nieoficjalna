import React from 'react';
import ReactDOM from 'react-dom/client';
import CarsView from "./components/CarsView";



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      {/*<BrowserRouter>*/}
      {/*    <App/>*/}
      {/*</BrowserRouter>*/}
      <CarsView/>

  </React.StrictMode>
);

