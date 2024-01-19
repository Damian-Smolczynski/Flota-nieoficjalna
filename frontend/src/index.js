import React from 'react';
import ReactDOM from 'react-dom/client';
import Popup from "./components/Popup";
import WidokPojazdow from "./components/WidokPojazdow";



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      {/*<BrowserRouter>*/}
      {/*    <App/>*/}
      {/*</BrowserRouter>*/}
      {/*<Popup/>*/}
      <WidokPojazdow/>

  </React.StrictMode>
);

